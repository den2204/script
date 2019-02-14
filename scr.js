javascript:(
    function() {
        moodlexchange=document.createElement('SCRIPT');
        moodlexchange.type='text/javascript';
        //moodlexchange.src='https://github.com/den2204/script/blob/master/main.js?random='+(new Date()).getTime();
        moodlexchange.src='https://raw.githubusercontent.com/den2204/script/master/main.js';
        //moodlexchange.src='https://cdn.jsdelivr.net/gh/alryaz/moodle-exchange/script.js?random='+(new Date()).getTime();
        //document.getElementsByTagName('head')[0].appendChild(moodlexchange);
        document.body.insertBefore(moodlexchange, document.body.firstChild);
        
    }
)();


