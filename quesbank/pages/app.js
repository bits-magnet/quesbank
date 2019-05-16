var myApp = angular.module('myApp',['ngRoute','ngTable','ngSanitize']);
var URL = "http://dummy.restapiexample.com/api/v1/employees";



myApp.controller('mainController', ['$scope','$http','$location','NgTableParams','$window', function($scope, $http, $location, NgTableParams, $window) {

    var urlParameter = getUrlParameters();
    getData($http,$scope,URL,{});

    $scope.tableParams = new NgTableParams({}, { dataset: $scope.data });

    var urlpath = getUrlPath($location);

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
  return paramsObject;
}

function getData($http,$scope,URL,urlParameter) {
  $http({
    method : "GET",
    url :  URL,
    //params : urlParameter,
  }).then(function (response,data) {
      console.log(response.data);
    $scope.data= response.data;
  });
}

function getUrlPath($location) {
  return $location.absUrl();
}
