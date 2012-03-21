$(function() {
    pollForSongData();
});

var pollForSongData = function() {
    console.log("Polling...");
    $.ajax("/identify/").success(function(data) {
        console.log("Success!");
        writeSongData(data);
        pollForSongData();
    }).error(function(data) {
        console.log("Error!");
        setTimeout(function() {
            pollForSongData();
        }, 1000);
    });
};

var writeSongData = function(data) {
    console.log(data);
    if(data.songs.length > 0) {

    }
}
