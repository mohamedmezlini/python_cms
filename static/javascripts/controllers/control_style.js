function change_style ($scope, $http) {
	$scope.json={};
	$scope.old_target="";
	$scope.text_decoration="";
	$scope.font_style="";
	$scope.font_size="";
	$scope.font_weight=";"
	$scope.font_variant="";
	$scope.police="";
	$scope.color="";
	$scope.text_align="";
	$scope.vertical_align="";
	$scope.line_height="";
	$scope.text_indent="";
	$scope.white_space1="";
	$scope.word_wrap="";
	$scope.text_shadow="";
	$scope.liste=[];
	$scope.liste1=[];
	$scope.liste_changeante=[];
	$scope.liste2=[];
	$scope.json_ok=[];
	$scope.font_select=""
	var_style=[];
	$scope.styles="";
	$scope.links=[];
	$scope.liste_decorations=["underline", "overline", "line-through", "none"];
	$scope.liste_halign=["left", "center", "right", "justify"];
	$scope.liste_valign=["baseline", "middle", "sub", "super", "top", "bottom"];
	$scope.liste_font_styles=["normal", "italic", "oblique"];
	$scope.liste_font_variants=["normal", "small-caps"];
	$scope.liste_font_weights=["normal", "bold"];

	var obj = new Object();
(function() {
			var url = 'https://www.googleapis.com/webfonts/v1/webfonts?key=AIzaSyDaI9pLFmYGBkEqTxtLE0tmArpAAH05zYQ';
			$.ajax({
			   type: 'GET',
			   url: url,
			   async: false,
			   jsonpCallback: 'jsonCallback',
			   contentType: "application/json",
			   dataType: 'jsonp',
			   success: function(data) {
			      $scope.json=data;
			    	var temp=[];
					for(i=0;i < $scope.json.items.length;i++){
						ch_temp=$scope.json.items[i].family.replace(' ','+');
						$scope.liste.push($scope.json.items[i].family);
						ch_temp1=ch_temp;
						for(j=0;j < $scope.json.items[i].variants.length;j++){
							ch_temp=ch_temp1;
							ch_temp=ch_temp+":"+$scope.json.items[i].variants[j];
							ch_temp2=ch_temp;
							for(k=0; k < $scope.json.items[i].subsets.length ;k++){
								ch_temp=ch_temp2;
								ch_temp=ch_temp+"&subset="+$scope.json.items[i].subsets[k];
								temp.push(ch_temp);
								}
						}	
					
					}
					
				$scope.json_ok=temp;
				$.each($scope.liste,function(cle, val){
					$scope.liste2.push({ "nom" : val });

				});
				$.each($scope.json_ok,function(cle, val){
					$scope.liste1.push({ "nom" : val });

				});
				

				console.log($scope.json_ok);

				console.log($scope.liste2);
			},
		    error: function(e) {
		       console.log(e.message);
			    }
			});

			})(jQuery);
	$scope.Api_google_fonts=function(){
		(function() {
			var url = 'https://www.googleapis.com/webfonts/v1/webfonts?key=AIzaSyDaI9pLFmYGBkEqTxtLE0tmArpAAH05zYQ';
			$.ajax({
			   type: 'GET',
			   url: url,
			   async: false,
			   jsonpCallback: 'jsonCallback',
			   contentType: "application/json",
			   dataType: 'jsonp',
			   success: function(data) {
			      $scope.json=data;
			    	var temp=[];
					for(i=0;i < $scope.json.items.length;i++){
						ch_temp=$scope.json.items[i].family.replace(' ','+');
						$scope.liste.push($scope.json.items[i].family);
						ch_temp1=ch_temp;
						for(j=0;j < $scope.json.items[i].variants.length;j++){
							ch_temp=ch_temp1;
							ch_temp=ch_temp+":"+$scope.json.items[i].variants[j];
							ch_temp2=ch_temp;
							for(k=0; k < $scope.json.items[i].subsets.length ;k++){
								ch_temp=ch_temp2;
								ch_temp=ch_temp+"&subset="+$scope.json.items[i].subsets[k];
								temp.push(ch_temp);
								}
						}	
					
					}
					
				$scope.json_ok=temp;
				$.each($scope.liste,function(cle, val){
					$scope.liste2.push({ "nom" : val });

				});
				$.each($scope.json_ok,function(cle, val){
					$scope.liste1.push({ "nom" : val });

				});
				

				console.log($scope.json_ok);

				console.log($scope.liste2);
			},
		    error: function(e) {
		       console.log(e.message);
			    }
			});

			})(jQuery);
		
	};

	$scope.selection_police = function(){
		var valeur=$(event.currentTarget).val();
		$scope.font_select=valeur;
		$scope.polices();	
		console.log(valeur);

		
	};

		
	$scope.text_shadows = function(){
		$scope.styles=$scope.styles+" #"+$scope.current_target+"{ text-shadow :"+$scope.text_shadow+";}";
		$('style').append("#"+$scope.current_target+"{ text-shadow :"+$scope.text_shadow+";}");
		
	};
	$scope.word_wraps = function(){
		$scope.styles=$scope.styles+" #"+$scope.current_target+"{ word-wrap :"+$scope.word_wrap+";}";
		$('style').append("#"+$scope.current_target+"{ word-wrap :"+$scope.word_wrap+";}");
		
	};
	$scope.white_spaces = function(){
		$scope.styles=$scope.styles+" #"+$scope.current_target+"{ white-space :"+$scope.white_space+";}";
		$('style').append("#"+$scope.current_target+"{ white-space :"+$scope.white_space+";}");
		
	};

	
	$scope.text_indents = function(){
		$scope.styles=$scope.styles+" #"+$scope.current_target+"{ text-indent :"+$scope.text_indent+";}";
		$('style').append("#"+$scope.current_target+"{ text-indent :"+$scope.text_indent+";}");
		
	};
	$scope.line_heights = function(){
		$scope.styles=$scope.styles+" #"+$scope.current_target+"{ line-height :"+$scope.line_height+";}";
		$('style').append("#"+$scope.current_target+"{ line-height :"+$scope.line_height+";}");
		
	};
	
	$scope.vertical_aligns = function(){
		$scope.styles=$scope.styles+" #"+$scope.current_target+"{ vertical-align :"+$scope.vertical_align+";}";
		$('style').append("#"+$scope.current_target+"{ vertical-align :"+$scope.vertical_align+";}");
		
	};
	
	$scope.text_decorations = function(){
		$scope.styles=$scope.styles+" #"+$scope.current_target+"{ text-decoration :"+$scope.text_decoration+";}";
		$('style').append("#"+$scope.current_target+"{ text-decoration :"+$scope.text_decoration+";}");
		
	};
	$scope.text_aligns = function(){
		$scope.styles=$scope.styles+" #"+$scope.current_target+"{ text-align :"+$scope.text_align+";}";
		$('style').append("#"+$scope.current_target+"{ text-align :"+$scope.text_align+";}");
		
	};
	$scope.font_styles = function(){
		$scope.styles=$scope.styles+" #"+$scope.current_target+"{ font-style :"+$scope.font_style+" ;}";
		$('style').append("#"+$scope.current_target+"{ font-style :"+$scope.font_style+" ;}");
		
	};
	$scope.font_variants = function(){
		$scope.styles=$scope.styles+" #"+$scope.current_target+"{ font-variant :"+$scope.font_variant+" ;}";
		$('style').append("#"+$scope.current_target+"{ font-variant :"+$scope.font_variant+" ;}");
		
	};
	$scope.font_weights = function(){
		$scope.styles=$scope.styles+" #"+$scope.current_target+"{ font-weight :"+$scope.font_weight+" ;}";
		$('style').append("#"+$scope.current_target+"{ font-weight :"+$scope.font_weight+" ;}");
		
	};
	
	$scope.font_sizes = function(){
		$scope.styles=$scope.styles+" #"+$scope.current_target+"{ font-size :"+$scope.font_size+"em;}";
		$('style').append("#"+$scope.current_target+"{ font-size :"+$scope.font_size+"em;}");
		
	};
	$scope.colors = function(){
		
		$scope.styles=$scope.styles+" #"+$scope.current_target+"{ color :"+$scope.color+";}";
		$('style').append("#"+$scope.current_target+"{ color :"+$scope.color+";}");
		
	};
	
	$scope.polices= function(){
		if ($scope.current_target != undefined) {
			link = "<link href='http://fonts.googleapis.com/css?family="+$scope.font_select.replace(" ","+")+"' rel='stylesheet' type='text/css'>";
		$('head').append(link);
		$scope.links.push(link);
		$('style').append("#"+$scope.current_target+"{ font-family :"+$scope.font_select+";}");
		$scope.styles=$scope.styles+" @import url(http://fonts.googleapis.com/css?family="+$scope.font_select.replace(" ","+")+");#"+$scope.current_target+"{ font-family :"+$scope.font_select+";}";
		console.log($scope.styles);
		console.log($scope.links);
		
		};
		 

	};
	$scope.save = function(){
		$http.post("http://localhost:5000/save",$scope.styles).success(function(data){
			$scope.styles="";
			console.log(data);
		});

	};	
	$scope.demo = function(){

	
		$($scope.old_target).attr("style", "");
		var html = ["The clicked div has the following styles:"];
		style= $(event.currentTarget).css(["width", "height", "color", "background-color"]);
		$scope.current_target = $(event.currentTarget).attr("id");

		console.log($scope.current_target);
		$(event.currentTarget).attr("style", "border : 3px dashed blue");
		$scope.old_target=event.currentTarget;
		event.stopPropagation();
		
		$.each( style, function( prop, value ) {
    		html.push( prop + ": " + value );
  			});
 
  		$( "#result" ).html( html.join( "<br>" ) );
  		console.log($(event.currentTarget).css(["width", "height", "color", "background-color"]));
  		console.log($(event.currentTarget)[0].style);
		};

}