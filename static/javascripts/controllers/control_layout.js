function change_layout ($scope, $http) {
	$scope.modify = true;
	$scope.add= false;
	$scope.pages=[];
	$scope.parts=[];
	$scope.current_page="";
	$scope.sub_parts=[];
	$scope.articles=[];	

  
  	
  
	$scope.old_target="";
	var total_columns= 12;

	$(document).ready(function() {
		$http.get("/get-site").success(function(data){
  		$scope.site = data;
  		var keys = Object.keys($scope.site);
  		for (key in keys){
  			if (keys[key] != "_id"){
  				$scope.pages.push({page:keys[key]});
  			}
  			
  		}		
  	});
 		
	});
	
	$scope.render_sub_content=function(){
		$("#injection div ").remove();
		$scope.string_injection="";
		$scope.sub_parts=[];
		$scope.articles=[];
		$scope.sub_parts=[];
		$scope.current_subtarget="";
		$scope.old_subtarget=event.currentTarget;
		$scope.current_subtarget = $(event.currentTarget).attr("id");
		event.stopPropagation();
		var keys = Object.keys($scope.site[$scope.current_target][$scope.current_subtarget]);

		for (key in keys){

			if((keys[key]!= "tag")&&(keys[key]!= "columns_total")&&(keys[key]!= "columns_current")&&(keys[key]!= "class")){ 
			
  				$scope.sub_parts.push({content: keys[key] });
 
  				$scope.string_injection="<div id='"+keys[key]+"' style='display: block ;text-align: center' class='well well-large, selection' ><p>"+keys[key]+"</p>";
  				
  				var articles= Object.keys($scope.site[$scope.current_target][$scope.current_subtarget][keys[key]]);
  				
  				for (article in articles){


  					if((articles[article]!= "text")&&(articles[article]!= "tag")&&(articles[article]!= "columns_total")&&(articles[article]!= "columns_current")&&(articles[article]!= "class")){ 
  						
  						current_columns= parseInt( $scope.site[$scope.current_target][$scope.current_subtarget][keys[key]][articles[article]]["columns_current"]);
  						
  						total_columns= parseInt( $scope.site[$scope.current_target][$scope.current_subtarget][keys[key]][articles[article]]["columns_total"]);
  						width=((current_columns/total_columns)*100)-1+"%";
  						$scope.articles.push({art: articles[article], width: width});
  						
  						$scope.string_injection= $scope.string_injection+"<div id='"+articles[article]+"' style='display: inline-block;width:"+width+";border : 1px dashed black'  ><p>"+articles[article]+"</p></div>";
						
  						
  						
  					}
  					
  				} 
  				$scope.string_injection= $scope.string_injection+"</div>";
  				$("#injection").append($scope.string_injection) ;
  			}
  			
  		}
  		
  		
  		
  		

	};
	$scope.render_articles=function(){
		 		

	};

	$scope.randomId = function (){
    return Math.random().toString(36).substring(7);

	};
	$scope.add_row = function(){
		
		console.log($scope.demo_var);
		$scope.demo_var="none";
		
	};
	$scope.modify_row = function(){
		console.log($scope.demo_var);
		$scope.demo_var="modif";

		
	};
	$scope.delete_row = function(){
		$scope.demo_var="del";
		console.log($scope.demo_var);
		
	};

	$scope.demo = function(){
		//var injection_tabs="<div class='tab-pane active'  id='"+$scope.current_target+"'><ul class='nav nav-tabs'>";
		$scope.parts=[];
		console.log($scope.site);
		$scope.current_target="";
		$scope.old_target=event.currentTarget;
		$scope.current_target = $(event.currentTarget).attr("id");
		var keys = Object.keys($scope.site[$scope.current_target]);

		for (key in keys){

  			$scope.parts.push({page: $scope.current_target, part:keys[key]});
  			//injection_tabs= injection_tabs+"<li ><a  href='#sub"+keys[key]+"' ng-click='render_sub_content()'   >"+keys[key]+"</li>";
  		}
  		/*injection_tabs=injection_tabs+"</ul>";		
  		console.log(injection_tabs);
  		$("#injection_tab").append(injection_tabs);*/

	};

	    
      

}	