var myApp = angular.module('myApp',['ngRoute','ngTable','ngSanitize']);
var URL1 = "http://127.0.0.1:8000/api/objective-question/";



myApp.controller('mainController', ['$scope','$http','$location','NgTableParams','$window', function($scope, $http, $location, NgTableParams, $window) {

    var urlParameter = getUrlParameters();
    getData($http,$scope,URL1,urlParameter);
    //console.log(urlParameter);
    $scope.tableParams = new NgTableParams({}, { dataset: $scope.data });
    $scope.topic_name = "topic";
    var urlpath = getUrlPath($location);

    $scope.editQuestion = function(question_id) {

      // Edit the Question
      console.log(question_id.id);
      $window.location.href = './question/' + question_id;
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
  return paramsObject;
}
// Data of Objective Question

function getData($http,$scope,URL,urlParameter) {
    console.log(urlParameter);
  $http({
    method : "GET",
    url :   "http://127.0.0.1:8000/api/objective-question/",
    params : urlParameter
  }).then(function (response,data) {
      //console.log(response.data);
    $scope.data= response.data;
  });
}

function getUrlPath($location) {
  return $location.absUrl();
}
