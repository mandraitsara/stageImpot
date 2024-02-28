$(document).ready(function(){

    $('.demande-de-stage').hide() //caché avant d'ouvrir de page

    $("#checkbox-stage").on("click", function(){
        window.location.replace("/blog/inscriptionStage/")
    })

    $('.dem-stage').click(function(){

        $('.demande-de-stage').toggle()
    })

    $('.comp-des-info').click(function(){
        $('.comp-des-info-active').toggle()
    })

    $('.notification-stage').click(function(){
        $('.notification-stage-active').toggle()
    })
})