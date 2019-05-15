from .models import *

def create_standard(standard):
    std, created = Standard.objects.get_or_create(standard = standard)
    std.save()

def get_standard(standard):
    return Standard.objects.get(standard = standard)

def create_subject(standard, subject):
    subj, created = Subject.objects.get_or_create(standard = standard, subject = subject)
    subj.save()

def get_standard(standard, subject):
    return Subject.objects.get(standard = standard, subject = subject)

def create_source(standard, source_name = '', source_type = ''):
    src, created = Source.objects.get_or_create(standard = standard, source_name = source_name, source_type = source_type)
    src.save()

def create_topic(subject, topic = '', topic_id = 0):
    tpc, created = Topic.objects.get_or_create(subject = subject, topic = topic, topic_id = topic_id)
    tpc.save()

def create_inquestion(topic, source, question_id = 'NA', question_html = 'NA', solution_html = 'NA', is_publish = 'NA',
                      is_active = 'NA', tc_map_id = 'NA', text_book_id = 'NA', chapter_id = 'NA', exercise_id = 'NA',
                      flow = 'NA', set_no = 'NA', page_flow = 'NA', page_no = 'NA', question_no = 'NA', exercise_flow = 'NA',
                      edition = 'NA', tc_map_is_active = 'NA', slo_id = 'NA', slo_map_id = 'NA', slo_mao_is_active = 'NA', exercise_name = 'NA'
                      ):
    inques, created = InQuestion.objects.get_or_create(topic, source, question_id = question_id, question_html = question_html, solution_html = solution_html, is_publish = is_publish,
                      is_active = is_active, tc_map_id = tc_map_id, text_book_id = text_book_id, chapter_id = chapter_id, exercise_id = exercise_id,
                      flow = flow, set_no = set_no, page_flow = page_flow, page_no = page_no, question_no = question_no, exercise_flow = exercise_flow,
                      edition = edition, tc_map_is_active = tc_map_is_active, slo_id = slo_id, slo_map_id = slo_map_id, slo_mao_is_active = slo_mao_is_active,
                        exercise_name = exercise_name)
    inques.save()
