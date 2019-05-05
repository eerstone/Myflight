var CookieUtils = {
		/**
		 * 保存cookie
		 */
		save:function(queryType){
			var exp = new Date();
			exp.setTime(exp.getTime() + 24*60*60*1000);//有效时间24小时
			//航班查询
			if(queryType=="FLIGHT"){
				var flightCode = $('#flightCode').val();
				var flightNo = $('#flightNo').val();
				var takeoffDate = $('#takeoffDate').val();
				var queryFlight = $.trim(flightCode)+","+$.trim(flightNo)+","+$.trim(takeoffDate);
				document.cookie = "queryFlight="+escape(queryFlight)+";expires=" + exp.toGMTString();
			}else if(queryType=="TRIP"){//行程查询
				var sl_start = $('#sl_start').val();
				var orgCity = $('#orgCity').val();
				var sl_end = $('#sl_end').val();
				var dstCity = $('#dstCity').val();
				var takeoffDate1 = $('#takeoffDate1').val();
				var queryTrip = $.trim(sl_start)+","+$.trim(orgCity)+","+$.trim(sl_end)+","+$.trim(dstCity)+","+$.trim(takeoffDate1);
				document.cookie = "queryTrip="+escape(queryTrip)+";expires=" + exp.toGMTString();
			}
	    },
	    /**
	     * 获取cookie
	     */
	    query:function(queryType){
	    	var queryTrip = "";
			var queryFlight = "";
			
			if(document.cookie.indexOf("queryTrip")>=0 || document.cookie.indexOf("queryFlight")>=0){
				var cookieValue = document.cookie.split(';');
				for(var i=0;i<cookieValue.length;i++){
					var cookieValueItem = cookieValue[i];
					if(cookieValueItem.indexOf("queryTrip")>=0){
						queryTrip = cookieValueItem.replace("queryTrip=", "");
						queryTrip = unescape(queryTrip).split(",");
					}
					if(cookieValueItem.indexOf("queryFlight")>=0){
						queryFlight = cookieValueItem.replace("queryFlight=", "");
						queryFlight = unescape(queryFlight).split(",");
					}
				}
				//行程查询
				if(queryType=="TRIP"){
					$('#sl_start').val($.trim(queryTrip[0]));
					$('#orgCity').val($.trim(queryTrip[1]));
					$('#sl_end').val($.trim(queryTrip[2]));
					$('#dstCity').val($.trim(queryTrip[3]));
					$('#takeoffDate1').val($.trim(queryTrip[4])==""?this.getTodayDate():$.trim(queryTrip[4]));
					
				}else if(queryType=="FLIGHT"){//航班查询
					$('#flightCode').val($.trim(queryFlight[0]));
					$('#flightNo').val($.trim(queryFlight[1]));
					$('#takeoffDate').val($.trim(queryFlight[2])==""?this.getTodayDate():$.trim(queryFlight[2]));
				}
			}else{
				$('#takeoffDate').val(this.getTodayDate());
				$('#takeoffDate1').val(this.getTodayDate());
			}
			if(document.cookie.indexOf("queryFlight")<0){
				$('#flightCode').val("HU");
			}
	    },
	    /**
		 * 临时保存cookie
		 */
		tempSave:function(name, value){
			document.cookie = name+"="+value;
	    },
	    /**
	     * 获取cookie
	     */
	    tempQuery:function(name,value){
	    	var result = "N";
	    	if(document.cookie.indexOf(name)<0){//为空
	    		result = "Y";
	    	}else if(document.cookie.indexOf(name+"="+value)>=0){//cookies有值
	    		result = "Y";
	    	}
			return result;
	    },
	    getTodayDate:function(){
	    	var date = new Date();
	        var seperator1 = "-";
	        var seperator2 = ":";
	        var month = date.getMonth() + 1;
	        var strDate = date.getDate();
	        if (month >= 1 && month <= 9) {
	            month = "0" + month;
	        }
	        if (strDate >= 0 && strDate <= 9) {
	            strDate = "0" + strDate;
	        }
	        var currentdate = date.getFullYear() + seperator1 + month + seperator1 + strDate;
	        return currentdate;
	    }
	    
}
