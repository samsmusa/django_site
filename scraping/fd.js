var http = require('http');
var fs = require('fs');

var arr = ['https://n2k3y9s6.stackpathcdn.com/wp-content/uploads/2021/12/conflicting-copy-malaysian-government-scholarship-2020-by-ministry-of-education-malaysia-2021-12-09t174010.636-min-100x70.jpg', 'https://n2k3y9s6.stackpathcdn.com/wp-content/uploads/2021/12/conflicting-copy-malaysian-government-scholarship-2020-by-ministry-of-education-malaysia-2021-12-09t125058.531-min-100x70.jpg', 'https://n2k3y9s6.stackpathcdn.com/wp-content/uploads/2021/12/conflicting-copy-malaysian-government-scholarship-2020-by-ministry-of-education-malaysia-2021-12-08t132434.780-min-100x70.jpg', 'https://n2k3y9s6.stackpathcdn.com/wp-content/uploads/2021/12/conflicting-copy-malaysian-government-scholarship-2020-by-ministry-of-education-malaysia-2021-12-07t131454.554-min-100x70.jpg', 'https://n2k3y9s6.stackpathcdn.com/wp-content/uploads/2021/12/conflicting-copy-malaysian-government-scholarship-2020-by-ministry-of-education-malaysia-2021-12-06t130337.635-min-100x70.jpg', 'https://n2k3y9s6.stackpathcdn.com/wp-content/uploads/2021/12/conflicting-copy-malaysian-government-scholarship-2020-by-ministry-of-education-malaysia-2021-12-04t133406.560-min-100x70.jpg', 'https://n2k3y9s6.stackpathcdn.com/wp-content/uploads/2021/12/conflicting-copy-malaysian-government-scholarship-2020-by-ministry-of-education-malaysia-2021-12-03t203914.055-min-100x70.jpg', 'https://n2k3y9s6.stackpathcdn.com/wp-content/uploads/2021/12/conflicting-copy-malaysian-government-scholarship-2020-by-ministry-of-education-malaysia-2021-12-03t180343.641-min-100x70.jpg', 'https://n2k3y9s6.stackpathcdn.com/wp-content/uploads/2021/12/conflicting-copy-malaysian-government-scholarship-2020-by-ministry-of-education-malaysia-2021-12-03t143859.548-min-100x70.jpg', 'https://n2k3y9s6.stackpathcdn.com/wp-content/uploads/2021/12/header800x400-min-100x70.png'];

for (var i = arr.length - 1; i >= 0; i--) {
    (function(url){
        var file = fs.createWriteStream(url.split('/').pop(-1).toLowerCase().replace("%20", "-"));
        http.get(url, function(response) {
            response.pipe(file);
        });
    })(arr[i]);
};