function change_pwd($scope , $http) {
  $scope.new_login="";
  $scope.new_pwd="";
  $scope.confirm_pwd="";
  $scope.new_mail="";
  $scope.permission="";
  $scope.error_login="";
  $scope.error_new_password="";
  $scope.error_confirm_password="";
  $scope.error_mail="";
  $scope.result="";
  $scope.error_permission="";

  
  $scope.input_control= function(){
    console.log($scope.old_pwd);
    if ($scope.new_login != ""){

      if($scope.new_pwd != ""){

        if ($scope.confirm_pwd != ""){

          if($scope.new_pwd == $scope.confirm_pwd){
            if($scope.new_mail !=""){
              console.log("kkkkkkkkkkkkkkkkkkkk"+$scope.permission+"hhhhhhhhhhhhhh")



              $scope.permission=$scope.permission.toLowerCase();
              console.log("kkkkkkkkkkkkkkkkkkkk"+$scope.permission+"hhhhhhhhhhhhhh")
              if($scope.permission !="" &&($scope.permission=="false" || $scope.permission=="true"))
              {
                $scope.result="";
              var req_post ={login: $scope.new_login, password: $scope.new_pwd, email: $scope.new_mail, permission: $scope.permission};
              console.log(req_post);
              $http.post("/update_users", req_post ).success(function(data){
               console.log(data);
               $scope.result= data;
                });
            }

            else
            {
              $scope.error_login="";
              $scope.error_new_password="";
              $scope.error_confirm_password="";
              $scope.error_mail="";
              $scope.error_permission="";
              $scope.error_permission="please enter a True or False";


            }
          }






            else
            {
              $scope.error_login="";
              $scope.error_new_password="";
              $scope.error_confirm_password="";
              $scope.error_mail="";
              $scope.error_permission="";
              $scope.error_mail="please enter a mail adress";


            }

        }

        else{
          $scope.error_login="";
          $scope.error_new_password="";
          $scope.error_confirm_password="";
          $scope.error_mail="";
          $scope.error_permission="";
          $scope.error_confirm_password="password doesn't match";

        }


        }
        else
        {
        $scope.error_login="";
        $scope.error_new_password="";
        $scope.error_confirm_password="";
        $scope.error_mail="";
        $scope.error_permission="";
          $scope.error_confirm_password= "please confirm your password ";
        }
        
      } 
        else{
        $scope.error_login="";
        $scope.error_new_password="";
        $scope.error_confirm_password="";
        $scope.error_mail="";
        $scope.error_permission="";
          $scope.error_new_password= "please enter a password";

        }

    }
    else{
    $scope.error_login="";
    $scope.error_new_password="";
    $scope.error_confirm_password="";
    $scope.error_mail="";
    $scope.error_permission="";
      $scope.error_login="please enter a login";

    }  
  };


  
}