var myApp = angular.module('myApp',['ngRoute','ngTable','ngSanitize']);
var URL = "http://dummy.restapiexample.com/api/v1/employees";



myApp.controller('mainController', ['$scope','$http','$location','NgTableParams','$window', function($scope, $http, $location, NgTableParams, $window) {

    var urlParameter = getUrlParameters();
    getData($http,$scope,URL,{});

    $scope.tableParams = new NgTableParams({}, { dataset: $scope.data });

    var urlpath = getUrlPath($location);

    console.log("URL Path",urlpath);

     $scope.view_topics = function(subject_id) {


      console.log("see Duplicates");
      console.log(subject_id);
      $window.location.href = '#';
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
