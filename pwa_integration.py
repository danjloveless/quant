"""
PWA Integration for QUANTFIN Society Research
Adds Progressive Web App capabilities to the Streamlit app
"""

def get_pwa_meta_tags():
    """Returns PWA meta tags for mobile app functionality"""
    return """
    <!-- PWA Meta Tags -->
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="apple-mobile-web-app-title" content="QUANTFIN">
    <meta name="application-name" content="QUANTFIN">
    <meta name="theme-color" content="#3282b8">
    
    <!-- Icons -->
    <link rel="icon" type="image/png" sizes="192x192" href="/static/icon-192.png">
    <link rel="icon" type="image/png" sizes="512x512" href="/static/icon-512.png">
    <link rel="apple-touch-icon" href="/static/icon-192.png">
    
    <!-- Manifest -->
    <link rel="manifest" href="/manifest.json">
    
    <!-- Service Worker Registration -->
    <script>
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', function() {
                navigator.serviceWorker.register('/service-worker.js').then(function(registration) {
                    console.log('ServiceWorker registration successful');
                }, function(err) {
                    console.log('ServiceWorker registration failed: ', err);
                });
            });
        }
    </script>
    """

def get_mobile_viewport():
    """Returns mobile viewport configuration"""
    return """
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    """