window.onload = function() {

	var address = '10.9.3.101';
	var port = 22;
	var username = 'user';
	var password = 'clico123!';
	var sciezka = 'python3 /home/user/Desktop/server.py';

    setTimeout(function() {
        if (wssh && typeof wssh.connect === 'function') {
            wssh.connect(address, port, username, password);
        } 
    }, 1000); 
 setTimeout(function() {
        wssh.send(sciezka);
    }, 3000);

};
