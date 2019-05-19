$(function() {
	//提示
	$(".tip-btn-tip").on('click', function() {
		//从这里 开始
		$(".tip-tip-box").fadeIn();
		$(".tip-tip-box-nei").animate({
			opacity: "1"
		}, function() {
			$(".tip-tip-box-nei").animate({
				opacity: "1"
			}, 1500, function() {
				$(".tip-tip-box-nei").animate({
					opacity: "0"
				}, 1000)
				$(".tip-success-bg").hide()
			})
		})
		//到这里 结束
	})
	//关闭弹出框
	$(".closes").on('click', function() {
		$('.eject').animate({
			top: "-100%",
		}, function() {
			$('.eject').hide();
		})
		$('.bg100').fadeOut();
	})
	function isTime(str)
	{
		var a = str.match(/^(\d{1,2}):(\d{1,2})$/);
		if (a == null) {return false;}
		console.log(a);
		if (a[1]>=24 || a[2]>=60 || a[1] < 0||a[2]<0)
			return false;
		return true;
	}
	function dateToString(d)
    {
    	var y= d.getFullYear();
    	var m= d.getMonth() + 1;
    	var d=d.getDate();
      //把日期2017-1-6 格式化为标准的 2017-01-06
      //判断数字的长度是否是1，如果是1那么前面加上字符0
		if(m.toString().length == 1) m= "0" + m;
		if(d.toString().length == 1) d= "0" + d;
		return y+"-"+m+"-"+d;
    }
	function datediff(inputdate)
    {
    	var d = new Date();
	    var nowdate = dateToString(d);
	    var d1 = nowdate.split('-');
		var d2 = inputdate.split('-');
		var date1 = new Date(d1[0],d1[1],d1[2]);
		var date2 = new Date(d2[0],d2[1],d2[2]);
		var dt1 = date1.getTime();
		var dt2 = date2.getTime();
		console.log(d1[0],d1[1],d1[2]);
		console.log(d2[0],d2[1],d2[2]);
		console.log(dt1,dt2,(dt2-dt1) / (24*60*60*1000));
		return (dt2-dt1) / (24*60*60*1000)
    }
	//错误提示
	function errors() {
		//从这里 开始
		$(".tip-errors-bg").fadeIn();
		$(".tip-errors-bg .tip-tip-box-nei").animate({
			opacity: "1"
		}, function() {
			$(".tip-errors-bg .tip-tip-box-nei").animate({
				opacity: "1"
			}, 2000, function() {
				$(".tip-errors-bg .tip-tip-box-nei").animate({
					opacity: "0"
				}, 1000)
				$(".tip-errors-bg").hide()
			})
		})
		//到这里 结束
	}
	//正确提示
	function add_submit(post_data,url) {
		//alert("添加sssss!")
		$.ajax({
			type: 'POST',
			url: url,
			data: post_data,
			dataType: 'json',
			success: function(data) {
				//data = JSON.parse(data);
				console.log(data);
                if (data["issucceed"] == "1")
					alert("添加成功!")
				else if (data["issucceed"] == "2")
					alert("已存在，添加失败!")
				else
					alert("未知错误，添加失败!")
			},
			error: function(xhr, type) {
				alert("添加失败!")
			}
		});
	}

	function search_airport_submit(post_data,url){
		location.href = "/Myflightadmin/Manager/search_airport/?airport=" + post_data['airport'] + "&city=" + post_data['city'];
	}

	function search_flight_submit(post_data,url){
		location.href = "/Myflightadmin/Manager/search_flight/?flight_id=" + post_data['flight_id'] + "&city_from=" + post_data['city_from'] + "&city_to=" + post_data['city_to']+"&datetime="+ post_data['datetime'];
	}
	function success() {
		//从这里 开始
		$(".tip-success-bg").fadeIn();
		$(".tip-success-bg .tip-tip-box-nei").animate({
			opacity: "1"
		}, function() {
			$(".tip-success-bg .tip-tip-box-nei").animate({
				opacity: "1"
			}, 2000, function() {
				$(".tip-success-bg .tip-tip-box-nei").animate({
					opacity: "0"
				}, 1000)
				$(".tip-success-bg").hide()
			})
		})
		//到这里 结束
	}
	//登录校验
	var str = /^1\d{10}$/; //手机号格式
	$(".login-btn").on('click',function() {
		var tel = $(".check-tel").val();
		var pwd = $(".check-pwd").val();
		if (!str.test(tel)) {
			errors();
			$(".errors").text("请输入正确的手机号");
			return false;
		}
		if (pwd == "" || pwd.length < 6) {
			errors();
			$(".errors").text("您的密码不正确");
			return false;
		} else {
			success();
			$(".success").text("恭喜您登录成功!");
			location.href = "active.html"
		}
	})
	//表单选中 check
	$(".input-check").on('click',function() {
		//alert("fsd")
		$(this).toggleClass("checked");
	})
	$(".one").on('click',function() {
		//alert("fsd")
		$(".two").toggle();
	})
	//校验
	$(".order-btn-add_manager").on('click',function() {
		var managername = $(".order-manager_name").val();
		var managerpsw = $(".order-manager_psw").val();
		if (managername == "") {
			errors();
			$(".errors").text("请输入管理名!").css("color","black");
			return false;
		}
		if (managerpsw == "") {
			errors();
			$(".errors").text("请输入管理密码!").css("color","black");
			return false;
		}
		else {
			var data = {};
			var url = '/Myflightadmin/add_manager/';
			data['username'] = managername;
			data['password'] = managerpsw;
			//success();
			add_submit(data,url);
			//$(".success").text("添加成功!").css("color","black");
		}
	})
	//添加航班校检
	$(".order-btn-add-flight").on('click',function() {
		var takeoff = $(".order-takeoff").val();
		var landing = $(".order-landing").val();
		var flightname = $(".order-flightname").val();
		var PDtime = $(".order-PDtime").val();
		var PLtime = $(".order-PLtime").val();
		var airlinename = $(".order-airlinename").val();
		var date = $("#takeoffDate").val();
		if (takeoff == "") {
			errors();
			$(".errors").text("请输入起飞地!").css("color","black");
			return false;
		}
		if (landing == "") {
			errors();
			$(".errors").text("请输入降落地!").css("color","black");
			return false;
		}
		if (flightname == "") {
			errors();
			$(".errors").text("请输入航班号!").css("color","black");
			return false;
		}
		if (PDtime == "") {
			errors();
			$(".errors").text("请输入计划起飞时间!").css("color","black");
			return false;
		}
		if (!isTime(PDtime)){
			errors();
			$(".errors").text("计划起飞时间格式错误!").css("color","black");
			return false;
		}
		if (PLtime == "") {
			errors();
			$(".errors").text("请输入计划降落时间!").css("color","black");
			return false;
		}
		if (!isTime(PLtime)){
			errors();
			$(".errors").text("计划到达时间格式错误!").css("color","black");
			return false;
		}
		if (airlinename == "") {
			errors();
			$(".errors").text("请输入航空公司!").css("color","black");
			return false;
		}
		if (date == ""){
			errors();
			$(".errors").text("请选择日期!").css("color","black");
			return false;
		}
		if (datediff(date) <= 0 || datediff(date) > 31){
			errors();
			$(".errors").text("只能添加未来30天范围的航班！请重新选择查询日期!").css("color","black");
			return false;
		}
		else {
			//success();
			var post_data = {};
			var url = '/Myflightadmin/add_flight/';
			post_data['departure'] = takeoff;
			post_data['arrival'] = landing;
			post_data['flight_id'] = flightname;
			post_data['plan_departure_time'] = PDtime;
			post_data['plan_arrival_time'] = PLtime;
			post_data['company'] = airlinename;
			post_data['datetime'] = date;
			add_submit(post_data,url);
			//$(".success").text("添加成功!").css("color","black");
		}
	})
	//添加机场校检
	$(".order-btn-add_airport").on('click',function() {
		var airport_name = $(".order-airport_name").val();
		var airport_city = $(".order-airport_city").val();
		var airport_tem = $(".order-airport_tem").val();
		var airport_wea = $(".order-airport_wea").val();
		if (airport_name == "") {
			errors();
			$(".errors").text("请输入机场名称!").css("color","black");
			return false;
		}
		if (airport_city == "") {
			errors();
			$(".errors").text("请输入机场城市!").css("color","black");
			return false;
		}
		if (airport_tem == "") {
			errors();
			$(".errors").text("请输入机场温度!").css("color","black");
			return false;
		}
		if (airport_wea == "") {
			errors();
			$(".errors").text("请输入机场天气").css("color","black");
			return false;
		}
		else {
			var post_data = {};
			var url = '/Myflightadmin/add_airport/';
			post_data['airport'] = airport_name;
			post_data['city'] = airport_city;
			post_data['temperature'] = parseInt(airport_tem) ;
			post_data['weather'] = airport_wea;
			add_submit(post_data,url);
 			//success();
			//$(".success").text("添加成功!").css("color","black");
		}
	})
	//按城市查找机场校检
	$(".order-btn-search_airport-city").on('click',function() {
		var airport_city = $(".order-city").val();
		if (airport_city == "") {
			errors();
			$(".errors").text("请输入机场所在城市!").css("color","black");
			return false;
		}
		else {
			//success();
			var post_data = {};
			var url = '/Myflightadmin/Manager/init_search_airport/';
			post_data['city'] = airport_city;
			post_data['airport'] = '';
			search_airport_submit(post_data,url);
			//$(".success").text("查找成功!").css("color","black");
		}
	})
	//按机场名称查找机场校检
	$(".order-btn-search_airport-name").on('click',function() {
		var airport_name = $(".order-airport_name").val();
		if (airport_name == "") {
			errors();
			$(".errors").text("请输入机场名称!").css("color","black");
			return false;
		}
		else {
			//success();
			var post_data = {};
			var url = '/Myflightadmin/Manager/init_search_airport/';
			post_data['airport'] = airport_name;
			post_data['city'] = '';
			search_airport_submit(post_data,url);
			//$(".success").text("查找成功!").css("color","black");
		}
	})
	//按航班号查找航班校检
	$(".order-btn-search_flight-name").on('click',function() {
		var flightname = $(".order-flightname").val();
		var date = $("#takeoffDate").val();
		if (flightname == "") {
			errors();
			$(".errors").text("请输入航班号!").css("color","black");
			return false;
		}
		if (date == ""){
			errors();
			$(".errors").text("请选择日期!").css("color","black");
			return false;
		}
		if (datediff(date) <= 0 || datediff(date) > 31){
			errors();
			$(".errors").text("只能修改未来30天范围的数据！请重新选择查询日期!").css("color","black");
			return false;
		}
		else {
			//success();
			var post_data = {};
			var url = '/Myflightadmin/Manager/init_search_flight/'
			post_data['flight_id'] = flightname;
			post_data['datetime'] = date;
			post_data['city_from'] = '';
			post_data['city_to'] = '';
			search_flight_submit(post_data,url);
			//$(".success").text("查找成功!").css("color","black");
		}
	})
	//按起降地查找航班校检
	$(".order-btn-search_flight-tofrom").on('click',function() {
		var takeoff = $(".order-takeoff").val();
		var landing = $(".order-landing").val();
		var date = $("#takeoffDate").val();
		if (takeoff == "") {
			errors();
			$(".errors").text("请输入起飞地!").css("color","black");
			return false;
		}
		if (landing == "") {
			errors();
			$(".errors").text("请输入降落地!").css("color","black");
			return false;
		}
		if (date == ""){
			errors();
			$(".errors").text("请选择日期!").css("color","black");
			return false;
		}
		if (datediff(date) <= 0 || datediff(date) > 31){
			errors();
			$(".errors").text("只能修改未来30天范围的数据！请重新选择查询日期!").css("color","black");
			return false;
		}
		else {
			//success();
			var post_data = {};
			var url = '/Myflightadmin/Manager/init_search_flight/'
			post_data['city_from'] = takeoff;
			post_data['city_to'] = landing;
			post_data['datetime'] = date;
			post_data['flight_id'] = '';
			search_flight_submit(post_data,url);

			//$(".success").text("查找成功!").css("color","black");
		}
	})

})
