'use strict';

angular.module('sbAdminApp')
    .service('promiseService', PromiseService);

function PromiseService($http) {
    var PROMISES_API = "/api/promises/{user}";
    
    var promiseService = {
        promisesIMade: [],
        promisesIAmTracking: []
    };
    
    // Load up them promises
    $http.get(PROMISES_API.replace("{user}", "me"))
        .then(
            function (response) {
                var promises = response.data;
                
                promiseService.promisesIAmTracking.splice(0, promiseService.promisesIAmTracking.length);
                angular.extend(promiseService.promisesIAmTracking, promises.promisesIAmTracking);

                promiseService.promisesIMade.splice(0, promiseService.promisesIMade.length);
                angular.extend(promiseService.promisesIMade, promises.promisesIMade);
                
                console.log(promiseService);
            },
            function (error) {
                cosole.log("ERROR: " + error);
            }
        );        
    
    return promiseService;
}