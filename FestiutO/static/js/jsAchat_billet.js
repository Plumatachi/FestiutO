function acheterBillet(idEvenement,types){
    print("heello");
    if(document.getElementById("carteInput").value != "" && document.getElementById("dateInput").value != "" && document.getElementById("verificationInput").value != ""){
        if(types == "evenement"){
            $.ajax({
                url: '/acheter_vrai_billet_evenement',
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
                url: '/acheter_Billet_journee',
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