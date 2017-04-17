'use strict';

var myapp = angular.module ('myapp', []);
 myapp.config(function($interpolateProvider) { 
      $interpolateProvider.startSymbol('[['); 
      $interpolateProvider.endSymbol(']]');
    });