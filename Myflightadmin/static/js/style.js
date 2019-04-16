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
	//定单校验
	$(".order-btn-add_manager").on('click',function() {
		var managername = $(".order-manager_name").val();
		var managerpsw = $(".order-manager_psw").val();
		if (managername == "") {
			errors();
			$(".errors").text("请输入管理名!").css("color","black");
			return false;
		}
		if (managerpsw== "") {
			errors();
			$(".errors").text("请输入管理密码!").css("color","black");
			return false;
		}
		else {
			success();
			$(".success").text("添加成功!").css("color","black");
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
		if (PLtime == "") {
			errors();
			$(".errors").text("请输入计划降落时间!").css("color","black");
			return false;
		}
		if (airlinename == "") {
			errors();
			$(".errors").text("请输入航空公司!").css("color","black");
			return false;
		}
		else {
			success();
			$(".success").text("添加成功!").css("color","black");
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
			success();
			$(".success").text("添加成功!").css("color","black");
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
			success();
			$(".success").text("查找成功!").css("color","black");
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
			success();
			$(".success").text("查找成功!").css("color","black");
		}
	})
	//按航班号查找航班校检
	$(".order-btn-search_flight-name").on('click',function() {
		var flight_name = $(".order-flightname").val();
		if (flight_name == "") {
			errors();
			$(".errors").text("请输入航班号!").css("color","black");
			return false;
		}
		else {
			success();
			$(".success").text("查找成功!").css("color","black");
		}
	})
	//按起降地查找航班校检
	$(".order-btn-search_flight-tofrom").on('click',function() {
		var takeoff = $(".order-takeoff").val();
		var landing = $(".order-landing").val();
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
		else {
			success();
			$(".success").text("查找成功!").css("color","black");
		}
	})
	
})
