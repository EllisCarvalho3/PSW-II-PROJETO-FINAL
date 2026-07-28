/*------------------------------------------------------------------
  Music Academy - Custom Animations & Template Integration
-------------------------------------------------------------------*/

'use strict';

(function ($) {
    $(window).on('load', function () {
        /*------------------
            Preloader / Carregamento
        --------------------*/
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");
    });

    /*------------------
        Background Set (Dinâmico)
        Pega o atributo data-setbg do HTML e injeta como inline CSS background
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    /*------------------
        Animação Suave de Rolagem (Smooth Scroll)
    --------------------*/
    $('.linear__icon a[href^="#"]').on('click', function (e) {
        e.preventDefault();
        var target = this.hash;
        var $target = $(target);
        if ($target.length) {
            $('html, body').stop().animate({
                'scrollTop': $target.offset().top
            }, 900, 'swing');
        }
    });

    /*------------------
        Magnific Popup (Vídeos/Modais semelhantes ao original)
    --------------------*/
    $('.play-btn').magnificPopup({
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false
    });

    /*------------------
        Barras de Progresso Animadas (Barfiller)
        Caso queira usar em páginas de detalhes ou relatórios
    --------------------*/
    if($('#bar1').length) { $('#bar1').barfiller({ barColor: '#5c00ce', duration: 2000 }); }
    if($('#bar2').length) { $('#bar2').barfiller({ barColor: '#5c00ce', duration: 2000 }); }
    if($('#bar3').length) { $('#bar3').barfiller({ barColor: '#5c00ce', duration: 2000 }); }

    /*------------------
        Comportamento Estético dos Players de Áudio
    --------------------*/
    $('.player_button').on('click', function () {
        var $btn = $(this);
        // Remove a classe tocando de outros players ativos
        $('.player_button').not($btn).removeClass('fa-pause').addClass('fa-play');
        
        // Alterna o estado visual do botão clicado
        if ($btn.hasClass('fa-play') || $btn.length === 0) {
            $btn.removeClass('fa-play').addClass('fa-pause');
        } else {
            $btn.removeClass('fa-pause').addClass('fa-play');
        }
    });

})(jQuery);