document.addEventListener("DOMContentLoaded", function () {
    // Find all links on the page
    document.querySelectorAll('a[href]').forEach(link => {
        // Add target="_blank" to external links (excluding internal ones)
        if (!link.href.startsWith(location.origin)) {
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
        }
    });
});
