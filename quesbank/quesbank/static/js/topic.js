var myApp = angular.module('myApp',['ngRoute','ngTable','ngSanitize']);

var URL1 = "http://127.0.0.1:8000/subjective-question/"
var URL2 = "http://127.0.0.1:8000/objective-question/"



myApp.controller('mainController', ['$scope','$http','$location','NgTableParams','$window', function($scope, $http, $location, NgTableParams, $window) {

	$scope.topic_data = '';
	$scope.subject_data = '';
	getTopicData($http,$scope);
	getSubjectdata($http,$scope);



	$scope.objective_imported = function() {
		$scope.state = "imported";
		$window.location.href = makeUrl(URL2, $scope.topic_id,$scope.state);

	}
	$scope.objective_created = function() {
		$scope.state = "created";
		$window.location.href = makeUrl(URL2, $scope.topic_id,$scope.state);
	}
	$scope.objective_processed = function() {
		$scope.state = "processed";
		$window.location.href = makeUrl(URL2, $scope.topic_id,$scope.state);
	}


	$scope.objective_duplicate = function() {

		$scope.state = "duplicate";
		$window.location.href = makeUrl(URL2, $scope.topic_id,$scope.state);
	}

	$scope.objective_rejected = function() {
		$scope.state = "rejected";
		$window.location.href = makeUrl(URL2, $scope.topic_id,$scope.state);
	}

	$scope.subjective_imported = function() {
		$scope.state = "imported";
		$window.location.href = makeUrl(URL1, $scope.topic_id,$scope.state);
	}
	$scope.subjective_created = function() {
		$scope.state = "created";
		$window.location.href = makeUrl(URL1, $scope.topic_id,$scope.state);
	}
	$scope.subjective_processed = function() {
		$scope.state = "processed";
		$window.location.href = makeUrl(URL1, $scope.topic_id,$scope.state);
	}

	$scope.subjective_duplicate = function() {
		$scope.state = "duplicate";
		$window.location.href = makeUrl(URL1, $scope.topic_id,$scope.state);
	}

	$scope.subjective_rejected = function() {
		$scope.state = "rejected";
		$window.location.href = makeUrl(URL1, $scope.topic_id,$scope.state);
	}

}]);

function makeUrl(URL, topic_id, state) {


    return URL + "?topic=" + topic_id + "&state="+state;
}

function getTopicData($http,$scope) {
  $http({
    method : "GET",
    url :   "http://127.0.0.1:8000/api/topic/" + $scope.topic_id,
  }).then(function (response,data) {
    $scope.topic_data= response.data;
  });
}

function getSubjectData($http,$scope) {
  $http({
    method : "GET",
    url :   "http://127.0.0.1:8000/api/subject/" + $scope.topic_data.subject,
  }).then(function (response,data) {
    $scope.subject_data= response.data;
  });
}
