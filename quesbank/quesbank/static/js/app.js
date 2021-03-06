var myApp = angular.module('myApp',['ngRoute','ngTable','ngSanitize']);
var URL = "http://127.0.0.1:8000/api/topic/";



myApp.controller('mainController', ['$scope','$http','$location','NgTableParams','$window', function($scope, $http, $location, NgTableParams, $window) {

    var urlParameter = getUrlParameters();
    getData($http,$scope,URL,{});
    console.log(urlParameter);
    $scope.tableParams = new NgTableParams({}, { dataset: $scope.data });
    $scope.topic_name = "topic";
    var urlpath = getUrlPath($location);
    console.log($scope.topic_name);
    console.log("URL Path",urlpath);

    $scope.editQuestion = function(question_id) {

      // Edit the Question
      console.log(question_id.id);
      $window.location.href = './question.html';
    }

     $scope.seeDuplicates = function(question_id) {


      console.log("see Duplicates");
      console.log(question_id);
      $window.location.href = './duplicate.html';
    }



}]);

function getUrlParameters() {
  var paramsObject = {}
  window.location.search.replace(/\?/,'').split('&').map(function(o){ paramsObject[o.split('=')[0]]= o.split('=')[1]});
  console.log(paramsObject);
  return paramsObject;
}

function getData($http,$scope,URL,urlParameter) {
  $http({
    method : "GET",
    url :  URL,
    params : urlParameter,
  }).then(function (response,data) {
      console.log(response.data);
    $scope.data= response.data;
  });
}

function getUrlPath($location) {
  return $location.absUrl();
}
