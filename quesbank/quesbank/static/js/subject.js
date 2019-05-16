var myApp = angular.module('myApp',['ngRoute','ngTable','ngSanitize']);
var URL1 = "http://127.0.0.1:8000/api/subject/";



myApp.controller('mainController', ['$scope','$http','$location','NgTableParams','$window', function($scope, $http, $location, NgTableParams, $window) {

    var urlParameter = getUrlParameters();
    var urlpath = getUrlPath($location);

//    URL1 =   getPrimaryKey(urlpath);
    getData($http,$scope,URL1+subjectId,urlParameter);


    $scope.tableParams = new NgTableParams({}, { dataset: $scope.data });


    console.log("URL Path",urlpath);

     $scope.view_questions = function(topic_id) {


      console.log("see Duplicates");
      $window.location.href = './' + subjectId + '/topic/'+topic_id;
    }




}]);

function getUrlParameters() {
  var paramsObject = {}
  window.location.search.replace(/\?/,'').split('&').map(function(o){ paramsObject[o.split('=')[0]]= o.split('=')[1]});
  return paramsObject;
}

function getData($http,$scope,URL,urlParameter) {
  $http({
    method : "GET",
    url :  URL,
    params : urlParameter,
  }).then(function (response,data) {
    $scope.data= response.data;
    $scope.subject_name = $scope.data.subject;
    $scope.standard = $scope.data.standard.standard;
  });
}

function getUrlPath($location) {
  return $location.absUrl();
}

function getPrimaryKey(urlpath) {
    split =  urlpath.split();

    return split[split.length -1];
}