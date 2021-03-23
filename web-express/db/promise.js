function foo() {
    setTimeout(function() {
    }, 100);
}

try {
    foo();
} catch(err) {
    console.log('something err');
}