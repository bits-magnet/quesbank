from django.views import generic
from ckeditor_uploader import image_processing
from django.core.files.storage import default_storage
from ckeditor_uploader import utils
from django.conf import settings
from qlsapp.models import Topic
import os
from ckeditor_uploader import views as ckviews
from django.views.decorators.csrf import csrf_exempt
from django.utils.module_loading import import_string
from django.utils.html import escape
from django.http import HttpResponse, JsonResponse

def _get_user_path(user):
    user_path = ''
	
	# If CKEDITOR_RESTRICT_BY_USER is True upload file to user specific path.
	RESTRICT_BY_USER = getattr(settings, 'CKEDITOR_RESTRICT_BY_USER', False)
	if RESTRICT_BY_USER:
		try:
			user_prop = getattr(user, RESTRICT_BY_USER)
		except (AttributeError, TypeError):
			user_prop = getattr(user, 'get_username')
		
		if callable(user_prop):
			user_path = user_prop()
		else:
			user_path = user_prop

	return user_path

def get_upload_filename(upload_name,custom_path,user):

	user_path = _get_user_path(user)

	# Generate date based path to put uploaded file.
	# If CKEDITOR_RESTRICT_BY_DATE is True upload file to date specific path.
	if getattr(settings, 'CKEDITOR_RESTRICT_BY_DATE', True):
		date_path = datetime.now().strftime('%Y/%m/%d')
	else:
		date_path = ''

	# Complete upload path (upload_path + date_path).
	upload_path = os.path.join(getattr(settings,'CKEDITOR_UPLOAD_PATH',''),custom_path,user_path, date_path)

	if (getattr(settings, 'CKEDITOR_UPLOAD_SLUGIFY_FILENAME', True) and
			not hasattr(settings, 'CKEDITOR_FILENAME_GENERATOR')):
		upload_name = utils.slugify_filename(upload_name)

	if hasattr(settings, 'CKEDITOR_FILENAME_GENERATOR'):
		generator = import_string(settings.CKEDITOR_FILENAME_GENERATOR)
		upload_name = generator(upload_name)

	return default_storage.get_available_name(
		os.path.join(upload_path, upload_name)
)

class CustomImageUploadView(ckviews.ImageUploadView):
	http_method_names = ['post']

	def post(self, request, **kwargs):
		"""
		Uploads a file and send back its URL to CKEditor.
		"""
		uploaded_file = request.FILES['upload']
		backend = image_processing.get_backend()

		ck_func_num = request.GET.get('CKEditorFuncNum')
		if ck_func_num:
			ck_func_num = escape(ck_func_num)

		# Throws an error when an non-image file are uploaded.
		if not getattr(settings, 'CKEDITOR_ALLOW_NONIMAGE_FILES', True):
			try:
				backend.image_verify(uploaded_file)
			except utils.NotAnImageException:
				return HttpResponse("""
					<script type='text/javascript'>
					window.parent.CKEDITOR.tools.callFunction({0}, '', 'Invalid file type.');
					</script>""".format(ck_func_num))

		saved_path = self._save_file(request, uploaded_file)
		
		if(str(saved_path).split('.')[1].lower() != 'gif'):
			self._create_thumbnail_if_needed(backend, saved_path)
		url = utils.get_media_url(saved_path).split("?")[0] #To avoid custom key on AWS

		if ck_func_num:
			# Respond with Javascript sending ckeditor upload url.
			return HttpResponse("""
			<script type='text/javascript'>
				window.parent.CKEDITOR.tools.callFunction({0}, '{1}');
			</script>""".format(ck_func_num, url))
		else:
			retdata = {'url': url, 'uploaded': '1','fileName': uploaded_file.name}
		
		return JsonResponse(retdata)

	@staticmethod
	def _get_custom_path(request):
		'''
		Use CKEDITOR ID TO FIND THE CUSTOME PATH
		'''
		ckeditor_custom_path = ''
		if 'topic_id' in request.GET:
			topic_id = request.GET['topic_id']
			topic = Topic.objects.get(id=topic_id)
			acad_tree = topic.get_acad_tree()
			ckeditor_custom_path = str(acad_tree['board'].board_name)+"/"\
			+str(acad_tree['medium'].medium_name)+"/"\
			+str(acad_tree['standard'].standard)+"/"\
			+str(acad_tree['subject_group'].subject_master.subject_name)+"/"\
			+str(acad_tree['subject'].subject_master.subject_name)+"/"\
			+str(acad_tree['topic'].topic_name)+"/"

		if 'type' in request.GET:
			assert request.GET['type'] in ['questionbank','content'], "Not Implemented"
			ckeditor_custom_path = request.GET['type']+'/'+ckeditor_custom_path
			
		return ckeditor_custom_path

	@staticmethod
	def _save_file(request,uploaded_file):
		custom_path = CustomImageUploadView._get_custom_path(request)
		filename = get_upload_filename(uploaded_file.name,custom_path,request.user)
		
		img_name, img_format = os.path.splitext(filename)
		IMAGE_QUALITY = getattr(settings, "IMAGE_QUALITY", 60)

		if(str(img_format).lower() == "png"):

			img = Image.open(uploaded_file)
			img = img.resize(img.size, Image.ANTIALIAS)
			saved_path = default_storage.save("{}.jpg".format(img_name), uploaded_file)
			img.save("{}.jpg".format(img_name), quality=IMAGE_QUALITY, optimize=True)

		elif str(img_format).lower() == "jpg" or str(img_format).lower() == "jpeg":

			img = Image.open(uploaded_file)
			img = img.resize(img.size, Image.ANTIALIAS)
			saved_path = default_storage.save(filename, uploaded_file)
			img.save(saved_path, quality=IMAGE_QUALITY, optimize=True)

		else:
			saved_path = default_storage.save(filename, uploaded_file)
		return saved_path

upload = csrf_exempt(CustomImageUploadView.as_view())
browse = ckviews.browse