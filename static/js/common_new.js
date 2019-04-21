/*! niewei 最后发布于： 2018-02-05 */
function input_blur(a) {
    var b = $(currentInput).val();
    "" == $.trim(b) && ($(currentInput).val(a), $(currentInput).css("color", "#9c9c9c"))
}
function input_focus(a, b) {
    currentInput = a,
    b == $(a).val() && ($(a).val(""), $(a).css("color", "#414141"))
}
function Cus_message_layer(a) {
    cus_date = c_date,
    flightNum = c_fnum,
    startEnd = c_cities,
    startTime = c_dplan,
    endTime = c_aplan,
    phoneNum = c_phone;
    var b, c;
    if ("cus_tr_sure" == a.attr("class") ? (b = $(a).parent().prev().find("span").html(), c = $(a).parents("ul").children().eq(1).children("input").val()) : (b = $(a).next().html(), c = phoneNum), cus_date && flightNum && startEnd && startTime && endTime && phoneNum) var d = a.attr("class"),
    e = layer.open({
        type: 1,
        title: !1,
        closeBtn: 0,
        shadeClose: !0,
        btn: ["确认订制", "我再想想"],
        cancel: function() {
            layer.close(e),
            /cus_me_identity/.test(d) && a.removeClass("on")
        },
        yes: function() {
            var b, f, g = $(".cus_body_head_lf").find("#fnum").text(),
            h = $(".cus_body_head_lf").find("#fdate").text(),
            i = $(".cus_me_phone").text(),
            j = $(".cus_body_head_ri").children("a").attr("data_dcode"),
            k = $(".cus_body_head_ri").children("a").attr("data_acode"),
            l = $('.cus_body_head_ri input[type="hidden"]').val();
            if ("cus_tr_sure" == d) {
                switch (f = c, $(a).parent().siblings().find(".cus_other_select").children(".pc_checkDateH1").children("span").text()) {
                case "接机人":
                    b = 1;
                    break;
                case "乘机人":
                    b = 0;
                    break;
                case "送机人":
                    b = 2
                }
                layer.close(e);
                for (var m = a.parents(".cus_other_tr").children("ul").children("li"), n = 0; n < m.length; n++) switch (n) {
                case 0:
                case 1:
                    m.eq(n).children("span").text(m.eq(n).find("input").val());
                    break;
                case 2:
                    m.eq(n).children("span").text(m.eq(n).find(".pc_checkDateH1").text())
                }
            } else if (/cus_me_identity/.test(d)) {
                f = i;
                for (var o = $(".cus_me_bUl").find(".cus_me_identity"), n = 0; n < o.length; n++) if (o.eq(n).hasClass("on")) switch (n) {
                case 0:
                    b = 1;
                    break;
                case 1:
                    b = 0;
                    break;
                case 2:
                    b = 2
                }
                layer.close(e)
            }
            $.ajax({
                url: getUrl("follow/Customer/smsAddOrder"),
                type: "POST",
                dateType: "json",
                data: {
                    fnum: g,
                    depCode: j,
                    arrCode: k,
                    fdate: h,
                    orderStyle: b,
                    mobile: i,
                    tel: f,
                    name: l
                },
                success: function(b) {
                    var c = JSON.parse(b);
                    layer.msg(c.msg),
                    c.status && ($(".cus_bar_4,.cus_bar_line li:last").addClass("blue"), "cus_tr_sure" == a.attr("class") ? (a.parents(".cus_other_tr").find("span").css({
                        display: "block"
                    }).siblings().hide(), $(".cus_other_table_wrap").append(new_dom)) : $(".cus_me_identity").parent("li").siblings().children(".cus_me_identity").addClass("sended"))
                }
            })
        },
        content: '<div class="customize_layer"><ul><li>' + cus_date + "</li><li>航班号：<span>" + flightNum + "</span></li><li>" + startEnd + "</li><li>起飞时间<span>" + startTime + "</span>&nbsp;&nbsp;到达时间<span>" + endTime + "</span></li><li>" + b + "：<span>" + c + "</span></li></ul></div>"
    })
}
function toggle_internation() {
    $(".model_box").find(".model_tel").remove(),
    $(".model_box").prepend(cityLine)
} !
function() {
    var a;
    this.feeyo = {
        selectCode: function(a, b) {
            $("body").on("click", a,
            function() {
                $(b).is(":hidden") && $(b).slideToggle(200),
                $(document).bind("mousedown", feeyo.CodeMouse)
            })
        },
        CodeMouse: function(a) {
            if (0 == $(a.target).parents(".country-container").length) $(".country-container").hide(),
            $(document).unbind("mousedown");
            else if ("list" != $(a.target).find(".record").context.className) return $(".modelcirarr").html($(a.target).find(".record").context.innerText),
            $(".model_tel label").html($($(a.target).find(".record").context.innerHTML).attr("data-code")),
            $(".country-container").hide(),
            !1
        },
        selectControl: function(a, b) {
            $(a).click(function() {
                $(b).slideToggle(200),
                $(document).bind("mousedown", feeyo.selectMouse)
            })
        },
        selectClick: function(a, b) {
            var c = b.replace(/\./, "#");
            $(b).click(function() {
                var b = $(a).text(),
                d = $(this).text();
                b != d && ($(c).show(), $(c).siblings("div").hide(), $(a).text(d)),
                $(this).parent().toggle(),
                $(document).unbind("mousedown", feeyo.selectMouse)
            })
        },
        selectMouse: function(a) {
            1 > $(a.target).parents(".drop").length && feeyo.closeSelect()
        },
        closeSelect: function() {
            0 < $(".drop .down").length && ($(".drop .down").hide(), $(document).unbind("mousedown", feeyo.selectMouse))
        },
        backToTop: function() {
            $("#F_GoTop").click(function() {
                return $("html, body").animate({
                    scrollTop: 0
                },
                400),
                !1
            })
        },
        getDay: function() {
            var a = new Date,
            b = 10 > a.getDate() ? "0" + a.getDate() : a.getDate();
            return a.getFullYear() + "-" + "01 02 03 04 05 06 07 08 09 10 11 12".split(" ")[a.getMonth()] + "-" + b
        },
        getSAgo: function() {
            var a = new Date;
            return a.setDate(a.getDate() - 7),
            sagod = 10 > a.getDate() ? "0" + a.getDate() : a.getDate(),
            a.getFullYear() + "-" + "01 02 03 04 05 06 07 08 09 10 11 12".split(" ")[a.getMonth()] + "-" + sagod
        },
        getOneYearAgo: function() {
            var a = new Date;
            return a.setFullYear(a.getFullYear() + 1),
            a.setDate(a.getDate() - 1),
            endDa = 10 > a.getDate() ? "0" + a.getDate() : a.getDate(),
            a.getFullYear() + "-" + "01 02 03 04 05 06 07 08 09 10 11 12".split(" ")[a.getMonth()] + "-" + endDa
        },
        getTwoMonthAgo: function() {
            var a = new Date,
            b = a.setMonth(a.getMonth() + 3);
            return a.setDate(a.getDate() - 1),
            b = 10 > a.getMonth() ? "0" + a.getMonth() : a.getMonth(),
            tmd = 10 > a.getDate() ? "0" + a.getDate() : a.getDate(),
            a.getFullYear() + "-" + b + "-" + tmd
        },
        getQueryParam: function(a) {
            var b = window.location.search.match(RegExp("(\\?|&)" + a + "(\\[\\])?=([^&]*)"));
            return "date" != a || b ? !!b && b[3] : feeyo.getDay()
        },
        focusus: function() {
            var a;
            $(".header .menu li").hover(function() {
                a = $(this).find(".menu-dropdown"),
                1 == a.length && a.addClass("animate")
            },
            function() {
                1 == a.length && a.removeClass("animate")
            }),
            $("#appd_wrap_close").click(function() {
                $("#fl_pop_wrap_cntr").animate({
                    left: "100%"
                },
                800,
                function() {
                    $(".sidebar-wrapper").css("bottom", "139px"),
                    $("#icon_open").show(),
                    $("#appd_wrap_default").hide()
                })
            }),
            $("#icon_open").click(function() {
                $("#appd_wrap_default").show(),
                $("#fl_pop_wrap_cntr").animate({
                    left: "0%"
                },
                800,
                function() {
                    $(".sidebar-wrapper").css("bottom", "180px"),
                    $("#icon_open").hide()
                })
            }),
            $(".index-sidebar .advice ,.sanjiaoWrap").hover(function() {
                $(this).find(".sns_box").show()
            },
            function() {
                $(this).find(".sns_box").hide()
            }),
            $(".fc_table_bar").on("click", ".fc_handle_cancel",
            function() {
                var a = $(this),
                b = a.parents(".fc_tableLi9").siblings(".fc_tableLi1").text(),
                c = a.parents(".fc_tableLi9").siblings(".fc_tableLi2").text(),
                d = a.parents(".fc_tableLi9").attr("dcode"),
                e = a.parents(".fc_tableLi9").attr("acode");
                if (! (c && d && e && b)) return ! 1;
                var f = "取消该条航班订制记录，您将不会再收到" + c + "航班的动态信息通知",
                g = layer.open({
                    type: 0,
                    title: !1,
                    content: f,
                    btn: ["确定", "我在想想"],
                    closeBtn: 0,
                    cancel: function() {
                        layer.close(g)
                    },
                    yes: function() {
                        layer.close(g),
                        $.ajax({
                            url: getUrl("follow/Customer/cancelOrder"),
                            type: "POST",
                            dateType: "json",
                            data: {
                                fnum: c,
                                depCode: d,
                                arrCode: e,
                                fdate: b
                            },
                            success: function(b) {
                                var c = JSON.parse(b);
                                layer.msg(c.msg),
                                c.status && a.parents(".fc_table_bar").remove()
                            }
                        })
                    }
                })
            }),
            $(".ywx_down_wrap").on({
                mouseenter: function() {
                    $(this).find(".ywx_dSlide").stop(!1, !0).slideDown(200)
                },
                mouseleave: function() {
                    $(this).find(".ywx_dSlide").stop(!1, !0).slideUp(200)
                }
            }),
            $(".fc_table_bar").on("click", ".fc_handle_delete_btn",
            function() {
                var a = $(this),
                b = a.parents(".fc_tableLi9").siblings(".fc_tableLi1").text(),
                c = a.parents(".fc_tableLi9").siblings(".fc_tableLi2").text(),
                d = a.parents(".fc_tableLi9").attr("dcode"),
                e = a.parents(".fc_tableLi9").attr("acode");
                if (! (b && c && d && e)) return ! 1;
                b = $.trim(b),
                c = $.trim(c);
                var f = b.split("-"),
                g = f[0] + "年" + f[1] + "月" + f[2] + "日",
                h = "确定删除" + g + c + "航班的订制记录吗?",
                i = a.parents(".fc_table_bar"),
                j = layer.open({
                    type: 0,
                    title: !1,
                    content: h,
                    btn: ["确定", "我在想想"],
                    closeBtn: 0,
                    cancel: function() {
                        layer.close(j)
                    },
                    yes: function() {
                        layer.close(j),
                        $.ajax({
                            url: getUrl("follow/Customer/delOrder"),
                            type: "POST",
                            dateType: "json",
                            data: {
                                fnum: c,
                                depCode: d,
                                arrCode: e,
                                fdate: b
                            },
                            success: function(a) {
                                var b = JSON.parse(a);
                                layer.msg(b.msg),
                                b.status && i.remove()
                            }
                        })
                    }
                })
            }),
            $("body").on("click",
            function(a) {
                $(a.target).closest("#fc_tableLi1").length < 1 && $("#customizeDate").hide(),
                $(a.target).closest("#fc_tableLi8").length < 1 && $("#customizeIdentity").hide()
            }),
            $(".cus_me_identity").on("click",
            function() {
                $(this).parent("li").siblings().children(".cus_me_identity").hasClass("sended") ? layer.msg("您已订制该航班，无需再次订制") : ($(this).addClass("on").parent("li").siblings().children(".cus_me_identity").removeClass("on"), Cus_message_layer($(this)))
            });
            var b = !1;
            $(".cus_other_table_wrap").on("click", ".cus_tr_sure",
            function() {
                for (var a = $(this).parents(".cus_other_tr").find("input"), c = /^(1((3[0-9])|47|5[0-9]|7[0-9]|8[0-9]))\d{8}$/, d = 0; d < a.length; d++) {
                    if ("" == a.eq(d).val()) return layer.msg(a.eq(d).attr("tip")),
                    !1;
                    if ("cus_other_p" == a.eq(d).attr("class")) {
                        if (!c.test(a.eq(d).val())) return layer.msg("您输入的手机号码格式不正确"),
                        !1;
                        b = !0
                    }
                }
                b && Cus_message_layer($(this))
            }),
            $(".cus_other_table_wrap").on("click", ".cus_other_select h1",
            function() {
                $(this).siblings("ul").stop(!1, !0).slideToggle(200);
                var a = $(this);
                $(this).siblings("ul").on("click", "li",
                function() {
                    a.children("span").text($(this).text()),
                    $(this).parent(".down").hide()
                }),
                $(document).bind("mousedown", feeyo.selectMouse)
            }),
            $("#changeData_pnEdit").on("click",
            function() {
                $("#editLayer").show()
            }),
            $("#editLayer").on("click", ".edi_close",
            function() {
                $("#editLayer").hide()
            }),
            $("body").on("click", ".internation_tip", toggle_internation)
        },
        inputFocus: function(a, b) {
            $(a).val() == b && ($(a).val(""), $(a).css("color", "#414141"))
        },
        inputBlur: function(a, b) {
            var c = $(a).val();
            "" == $.trim(c) && ($(a).val(b), $(a).css("color", "#9c9c9c"))
        },
        windowSize: function() {
            return win_sise = {
                winvw: window.screen.availWidth,
                winvh: window.screen.availHeight,
                winsw: $(window).width(),
                winsh: $(window).height()
            }
        },
        fy_widget: function() {
            try {
                window.console && window.console.log && (console.log("%c Feeyo %c Copyright © 2005-%s", 'font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;font-size:64px;color:#2088c2;-webkit-text-fill-color:#00bbee;-webkit-text-stroke: 1px #00bbee;', "font-size:12px;color:#999999;", (new Date).getFullYear()), console.log("\n%c 如果你想来飞友工作", "color:#333;font-size:14px;"), console.log("\n 请将简历发送至 HR@variflight.com"))
            } catch(a) {}
        },
        openModel: function(b, c) {
            void 0 != a && a.close().remove(),
            a = dialog({
                fixed: !0,
                title: b,
                content: c
            }),
            a.showModal(),
            feeyo.selectCode(".modelcirarr", ".country-container"),
            $(".model_tel input").focus(function() {
                $(this).parent().find(".warnin").css("opacity", "0"),
                $(this).parent().find(".success").hide().css("opacity", "0")
            }),
            feeyo.tipHover("#internation_tip", "#internationTipBox"),
            start_ie8placeholder()
        },
        usercenter_m: function(a, b) {
            $(a).hover(function() {
                $(b).show()
            },
            function() {
                $(b).hide()
            })
        },
        tipHover: function(a, b) {
            $(b).height(),
            $(a).on({
                mouseenter: function() {
                    $(b).stop(!0, !1).show()
                },
                mouseleave: function() {
                    $(b).stop(!0, !1).hide()
                }
            })
        },
        selectListCheck: function(a, b) {
            $(b).find("li").on("click",
            function() {
                $(a).text($(this).text()),
                $(b).hide()
            })
        },
        tagToggle: function(a, b) {
            $(a).on("click",
            function() {
                var a = $(this).index(),
                c = $(this).position().left;
                $(this).siblings("#chBar").stop(!0, !1).animate({
                    left: c
                },
                300),
                $(b).eq(a).stop().show().siblings().stop(!0, !1).hide()
            })
        },
        swichBtn: function(a) {
            var b = $(a).children("a");
            b.on("click",
            function() {
                var a = $(this).position().left,
                c = $(this).index();
                b.eq(1 - c).position().left,
                $(this).siblings(".toggleSpan").stop(!0, !1).animate({
                    left: a + "px"
                },
                200).end().addClass("on").siblings("a").removeClass("on")
            })
        }
    }
} (),
$(document).ready(function() {
    feeyo.backToTop(),
    feeyo.focusus(),
    feeyo.fy_widget(),
    feeyo.usercenter_m(".usercenter_m", ".usercenter_m .menu-dropdown-inner"),
    feeyo.selectControl("#pc_checkDateH1", "#pc_checkDateUl"),
    feeyo.selectListCheck("#pc_checkDateH1 span", "#pc_checkDateUl"),
    feeyo.tipHover("#pcIcon_tip", "#pcIconTipBox"),
    feeyo.tipHover("#pcIcon_tip2", "#pcIconTipBox2"),
    feeyo.selectControl("#fc_tableLi1", "#customizeDate"),
    feeyo.selectControl("#fc_tableLi8", "#customizeIdentity"),
    feeyo.tagToggle(".changeDataTitle a", ".changeDataBody>div"),
    feeyo.swichBtn(".toggle_person")
});
