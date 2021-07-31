/*------------------------포매팅함수------------------------*/
function format() { var args = Array.prototype.slice.call (arguments, 1); 
    return arguments[0].replace (/\{(\d+)\}/g, function (match, index) { return args[index]; }); }


/*------------------------초기화------------------------*/
$('.question').hide();

$('h3').eq(1).hide(); //두번째 h3 선택질문 설명 문구 가리기

$('input[type=submit]').hide();

$('.previous').css('opacity', '0');

let q_num = 22; //질문 개수

/*------------------------다음/이전 기능------------------------*/
var answer_cnt = 0;
var $question_list = $('.question');
var nextClickCnt = 1;   

$question_list.eq(answer_cnt).show();
//이전or다음 버튼을 연속 클릭 했을 시 애니메이션 빠르게 적용하기위해 nextClickCnt사용
$('.next').on('click', function(){
    // if (vaildation() == true){
        if(answer_cnt == 0) {
            $('.previous').animate({
                opacity: '1'
            }, 200);
        }
        if(answer_cnt != q_num){
            setTimeout(function(){
                $question_list.eq(answer_cnt).fadeOut(600/nextClickCnt);
                answer_cnt += 1;
                nextClickCnt += 10;
            }, 0);
            setTimeout(function(){
                nextClickCnt -= 10;
                $question_list.eq(answer_cnt).fadeTo(600/nextClickCnt, 1);
            }, 700);

            // $question_list.eq(answer_cnt).fadeOut(600);
            // answer_cnt += 1;
            // $question_list.eq(answer_cnt).delay(700).fadeIn(600);
        }
        if(answer_cnt == 13){
            $(".next, .previous").animate({
                'opacity': '0'
            });
            $(".container").css('height', 'auto');
            $question_list.show();
        }
        reloadProgressBar();
    // }
})

$('.previous').on('click', function(){
    if(answer_cnt == 1) {
        $('.previous').animate({
            'opacity': '0',
        }, 200);
    }
    if(answer_cnt != 0) {
        setTimeout(function(){
            $question_list.eq(answer_cnt).fadeOut(600/nextClickCnt);
            answer_cnt -= 1;
            nextClickCnt += 10;
        }, 0);
        setTimeout(function(){
            nextClickCnt -= 10;
            $question_list.eq(answer_cnt).fadeTo(600/nextClickCnt, 1);
        }, 700);
        // $question_list.eq(answer_cnt).fadeOut(600);
        // answer_cnt -= 1;
        // $question_list.eq(answer_cnt).delay(700).fadeIn(600);
    }
    reloadProgressBar();
})

$('.next, .previous').on('mouseover', function(){
    $(this).animate({
        // 'font-size' : '20px'
        color: '#000'
    }, 50, "swing");
})

$('.next, .previous').on('mouseleave', function(){
    $(this).animate({
        // 'font-size' : '15px'
        color: '#fff'
    }, 50, "swing");
})

/*------------------------진행바 구현------------------------*/
//1. 필수 문항/ 선택 문항 구분 필요
/*--------------------------------------------------------*/
function changeFrontBarWidth(width){
    $('.front-bar').animate( {
        width: format('{0}%', width)
      }, 400/nextClickCnt, 'swing' );
    
}

$('.front-bar > .text').css('opacity', '0')
function reloadProgressBar(){
    //질문 수에 따라 진행바 길이 조절
    if(answer_cnt + 1 == 0) changeFrontBarWidth(0);
    else changeFrontBarWidth(5 + (answer_cnt + 1) * 5);
    // console.log("질문 현황", answer_cnt);
    //진행상황 글자가 넘쳐서 front-bar가 어느정도 길어지면 나오게
    if(answer_cnt + 1 >= 3){
        setTimeout(function(){
            $('.front-bar > .text').animate( {
                opacity: "1"
            }, 600, "swing");
        }, 10);
    }
    
    //이전 페이지 버튼 
    if(answer_cnt < 3){
        setTimeout(function(){
            $('.front-bar > .text').animate( {
                opacity: "0"
            }, 600, "swing");
        }, 10);
    }
}

/*------------------------유효성 검사------------------------*/
//값을 선택해야 넘어가도록
//여기선 anw = answer

let anw_arr = $(".answer");

function vaildation(){ 
    var rt = true;
    var anw_cur = anw_arr.eq(answer_cnt);
    var anw_cur_type = anw_cur.children().eq(0).attr("type");
    var anw_cur_name = anw_cur.children().eq(0).attr("name");
    console.log(anw_cur_type, anw_cur_name);
    //라디오가 많으므로 라디오는 먼저!
    if(anw_cur_type == "radio"){
        if($('input[name="'+anw_cur_name+'"]:checked').val() == null) rt = false;
    }
    else if(anw_cur_type == "checkbox"){
        var anw_checkbox_arr = anw_cur.children("input[type=checkbox]");
        var checkbox_cnt = 0;
        $.each(anw_checkbox_arr, function(index, item){
            if(item.checked) cnt++;
        })
        if (anw_cur.children("input[type=text]").val().length != 0) cnt++;
        if(checkbox_cnt == 0) rt = false;
    }
    else if(anw_cur_type == "text" || anw_cur_type == "number"){
        if (anw_cur.children("input[type=text], input[type=number]").val().length == 0) rt = false;
    }
    else if(anw_cur_type == "time"){
        var time_list = anw_cur.children("input[type=time]");
        $.each(time_list, function(index, item){
            console.log($(this).val().length);
            if($(this).val().length == 0) rt = false;
        })
    }

    return rt;
}

