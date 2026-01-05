// Mobile Menu Toggle
const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const navMenu = document.querySelector('.nav-menu');

mobileMenuToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    mobileMenuToggle.querySelector('i').classList.toggle('fa-bars');
    mobileMenuToggle.querySelector('i').classList.toggle('fa-times');
});

// Close mobile menu when clicking on a link
const navLinks = document.querySelectorAll('.nav-menu a');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        mobileMenuToggle.querySelector('i').classList.add('fa-bars');
        mobileMenuToggle.querySelector('i').classList.remove('fa-times');
    });
});

// Smooth Scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 80,
                behavior: 'smooth'
            });
        }
    });
});

// Form Submission
const heroForm = document.querySelector('.hero-form form');
if (heroForm) {
    heroForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Get form values
        const name = this.querySelector('input[type="text"]').value;
        const phone = this.querySelector('input[type="tel"]').value;
        
        // Simple validation
        if (name && phone) {
            // In a real application, you would send this data to a server
            alert('Thank you for your interest! We will contact you soon.');
            this.reset();
        } else {
            alert('Please fill in all required fields.');
        }
    });
}

// Contact Form Submission
const contactUsForm = document.getElementById('contactUsForm');
if (contactUsForm) {
    contactUsForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Get form values
        const name = this.querySelector('input[name="name"]').value;
        const phone = this.querySelector('input[name="phone"]').value;
        const email = this.querySelector('input[name="email"]').value;
        const enquiryType = this.querySelector('select[name="enquiry-type"]').value;
        const message = this.querySelector('textarea[name="message"]').value;
        
        // Simple validation
        if (name && phone && email && enquiryType && message) {
            // In a real application, you would send this data to a server
            alert('Thank you for your message! We will contact you soon.');
            this.reset();
        } else {
            alert('Please fill in all required fields.');
        }
    });
}

// Animation on Scroll
const animateOnScroll = () => {
    const elements = document.querySelectorAll('.amenity-item, .three-d-item, .feature-item');
    
    elements.forEach(element => {
        const elementPosition = element.getBoundingClientRect().top;
        const screenPosition = window.innerHeight / 1.3;
        
        if (elementPosition < screenPosition) {
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }
    });
};

// Set initial state for animated elements
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll('.amenity-item, .three-d-item, .feature-item');
    
    animatedElements.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    });
    
    // Trigger animation on scroll
    window.addEventListener('scroll', animateOnScroll);
    
    // Initial check in case elements are already in view
    animateOnScroll();
});

// Header scroll effect
window.addEventListener('scroll', () => {
    const header = document.querySelector('.header');
    if (window.scrollY > 100) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// Download Map PDF functionality
const downloadPdfBtn = document.querySelector('.download-pdf-btn');

if (downloadPdfBtn) {
    downloadPdfBtn.addEventListener('click', async function(e) {
        e.preventDefault();
        console.log('Download PDF button clicked');
        // Define the path to your PDF
        const pdfUrl = 'images/skyrise-residential-township-map.pdf';
        const fileName = 'SkyRise-Residential-Township-Map.pdf';

        try {
            // Optional: Show loading state (e.g., change button text)
            const originalText = downloadPdfBtn.textContent;
            downloadPdfBtn.textContent = 'Downloading...';
            downloadPdfBtn.style.opacity = '0.7';

            // Check if file exists before trying to download
            const response = await fetch(pdfUrl, { method: 'HEAD' });

            if (response.ok) {
                // File exists, proceed with download
                const link = document.createElement('a');
                link.href = pdfUrl;
                link.download = fileName;
                link.target = '_blank';
                
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            } else {
                throw new Error('File not found');
            }
        } catch (error) {
            console.error('Download failed:', error);
            alert('Sorry, the map PDF is currently unavailable. Please contact support.');
        } finally {
            // Reset button state
            downloadPdfBtn.textContent = originalText || 'Download PDF'; // Fallback text if original was empty
             if (typeof originalText !== 'undefined') { //Check if originalText is defined before using it
                 downloadPdfBtn.textContent = originalText;
             }
            downloadPdfBtn.style.opacity = '1';
        }
    });
}