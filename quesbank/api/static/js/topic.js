var myApp = angular.module('myApp',['ngRoute','ngTable','ngSanitize']);


myApp.controller('mainController', ['$scope','$http','$location','NgTableParams','$window', function($scope, $http, $location, NgTableParams, $window) {

	$scope.topic_id = "";
	$scope.state = "";


	$scope.objective_new = function() {

		$scope.state = "created";

	}

	$scope.objective_duplicate = function() {

		$scope.state = "duplicate";

	}

	$scope.objective_rejected = function() {
		$scope.state = "rejected";
	}

	$scope.subjective_new = function() {
		$scope.state = "created";
	}

	$scope.subjective_duplicate = function() {
		$scope.state = "duplicate";
	}

	$scope.subjective_rejected = function() {
		$scope.state = "rejected";
	}

}]);
