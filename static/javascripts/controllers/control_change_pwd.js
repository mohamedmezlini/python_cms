function change_pwd($scope,$http) {
  $scope.old_pwd="";
  $scope.new_pwd="";
  $scope.confirm_pwd="";
  $scope.error_old="";
  $scope.error_new="";
  $scope.error_confirm="";
  $scope.result="";

  function getCookie(sName) {
        var cookContent = document.cookie, cookEnd, i, j;
        var sName = sName + "=";
  
        for (i=0, c=cookContent.length; i<c; i++) {
                j = i + sName.length;
                if (cookContent.substring(i, j) == sName) {
                        cookEnd = cookContent.indexOf(";", j);
                        if (cookEnd == -1) {
                                cookEnd = cookContent.length;
                        }
                        return decodeURIComponent(cookContent.substring(j, cookEnd));
                }
        }       
        return null;
}
  
  $scope.input_control= function(){
    if ($scope.old_pwd != ""){

      if($scope.new_pwd != ""){

        if ($scope.confirm_pwd != ""){

          if($scope.new_pwd == $scope.confirm_pwd){
             $scope.result="";

            console.log(getCookie("username"));
            var req_post ={login: getCookie("username"), old_password: $scope.old_pwd, new_password: $scope.new_pwd};
            console.log(req_post);
            $http.post("/update_user", req_post ).success(function(data){ console.log(data);$scope.result= data; });

        }

        else{
          $scope.error_old="";
          $scope.error_new="";
          $scope.error_confirm="";
          $scope.error_confirm="password doesn't match";

        }


        }
        else
        {
          $scope.error_old="";
          $scope.error_new="";
          $scope.error_confirm="";
          $scope.error_confirm= "please confirm your new password ";
        }
        
      } 
        else{
          $scope.error_new="";
          $scope.error_old="";
          $scope.error_confirm=""
          $scope.error_new= "please enter a new password";

        }

    }
    else{
      $scope.error_old="";
      $scope.error_new="";
      $scope.error_confirm=""
      $scope.error_old="please enter your old password";

    }  
  };


  
}