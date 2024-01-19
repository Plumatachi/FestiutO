function acheterBillet(idEvenement){
    if(document.getElementById("carteInput").value != "" && document.getElementById("dateInput").value != "" && document.getElementById("verificationInput").value != ""){
        console.log(types+" a");
        if(types == "evenement"){
            $.ajax({
                url: '/achat_billet',
                type: 'GET',
                data: {
                    "idEvenement" : idEvenement
                },
                success: function (data) {
                        alert(data);
                }
            });
        }
        else{
            $.ajax({
                url: '/achat_billet',
                type: 'GET',
                data: {
                    "idJournee" : idJournee,
                    "nombre" : nombreJournee,
                },
                success: function (data) {
                        alert(data);
                }
            });
        }
    }
}