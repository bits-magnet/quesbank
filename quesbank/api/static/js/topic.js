var myApp = angular.module('myApp',['ngRoute','ngTable','ngSanitize']);

var URL1 = "http://127.0.0.1:8000/subjective-question/"
var URL2 = "http://127.0.0.1:8000/objective-question/"



myApp.controller('mainController', ['$scope','$http','$location','NgTableParams','$window', function($scope, $http, $location, NgTableParams, $window) {

	$scope.topic_id = topicId;
	$scope.state = "";


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

	$scope.objective_approved = function() {
		$scope.state = "approved";
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
	$scope.subjective_approved = function() {
		$scope.state = "approved";
		$window.location.href = makeUrl(URL1, $scope.topic_id,$scope.state);
	}

}]);

function makeUrl(URL, topic_id, state) {
    return URL + "?topic=" + topic_id + "&state="+state;
}

