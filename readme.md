# StrayHelp 

Team Name: Yukti  

---

## Problem Statement
Stray animals frequently suffer from injuries and neglect due to delayed rescues and lack of coordination between citizens and NGOs. Although people often wish to help, they cannot always provide timely assistance. Currently, there is no efficient system that allows quick reporting, verification, and response to such cases. This gap leads to unnecessary suffering of animals that could otherwise be rescued.

---

## Project Overview
StrayHelp is a digital platform that connects citizens with NGOs to enable faster and more effective stray animal rescues. Users can report strays with images and location, while AI verifies the animal, assesses wound severity, and classifies breed. NGOs receive real-time alerts within their operational area, allowing them to take prompt action and update rescue status. By streamlining reporting, verification, and response, StrayHelp reduces delays and ensures timely care for stray animals.

---
## Link of demo : https://drive.google.com/drive/folders/126hWz1A4kZSk_T_3pwBddV_K47pb0J-Q?usp=drive_link

---
## Features & Workflows

### User Workflow
1. Register / Log In 
   - Users create an account or log in to the platform.  

2. Report a Stray Animal  
   - Upload an image of the animal.  
   - The system incorporates an AI-based image validation mechanism that automatically detects whether an uploaded image  contains an animal. If the image does not contain an animal, the upload is rejected, and the user is prompted to submit a valid image
   - System fetches the user’s current location or allows manual input.  
   
3. Dashboard creation  
   - The analyzed information (image, location, animal breed) is saved in the database and display it on dashboard.  

4. User Dashboard
   - Track submitted reports and receive status updates from NGOs.

### NGO Workflow
1. Register / Log In 
   - NGO staff creates an account and sets their operational area.  

2. NGO Dashboard
   - Lists new reports within their area.  
   - Each report displays:  
     - Animal image  
     - Location on map  
     - Animal type & breed    
     - Timestamp  

3. NGO Action 
   - Accept a report to begin rescue.  
   - Update status: In Progress / Resolved.  

4. Rescue Status Updates
   - Users are notified of the rescue progress and resolution.

---

## Tech Stack
- Backend: Django  
- Frontend: HTML, Bootstrap  
- Database: SQLite  
- AI Integration: Gemini API  (gemini-1.5-flash)

---

## Project Status
- Fully functional prototype connecting citizens and NGOs.  
- AI-based animal verification integrated.  
- Ready for testing and deployment.  

---
## Future Scope
- Smarter Breed Identification
  AI will recognize not just common pets but also mixed and local breeds, helping with quicker medical care and lost pet recovery.
  Revenue: Premium pet ID services for vets, shelters, and insurers.

- Instant Rescue Alerts
  A real-time rescue network will notify nearby NGOs, vets, and volunteers based on location.
  Revenue: SaaS partnerships with NGOs and city bodies.

- Transparent Donations & Sponsorships
  People can sponsor animals or treatments and track their impact with updates.
  Revenue: Transaction fees, CSR collaborations, and featured sponsorships.

- Volunteer Management Hub
  A system for registering, training, and scheduling volunteers, making rescues more organized.
  Revenue: Partnerships with colleges and corporates for CSR credits and certifications.

- Safe Adoption Platform
  Verified adopters, health records, and breed details to make adoption trustworthy.
  Revenue: Small processing fees or NGO subscriptions.

- Emergency HealthBot
  An AI chatbot for quick first-aid, feeding tips, and emergency steps until help arrives.
  Revenue: Paid upgrades for vet tele-consultation and premium advice.

- Better Image Validation
  Smarter AI filters to block irrelevant uploads and keep posts authentic.
  Revenue: Sell as an API to other pet-care platforms.

💡 Business Model

Freemium: Free reporting for users, premium features for NGOs and sponsors.

SaaS: Paid dashboards & analytics for NGOs and municipalities.

CSR & Donations: Partner with corporates for CSR funding.

Value-Adds: Vet consults, adoption services, and sponsorship programs.

## Team contribution

1. Smita Bhoine : Backend Development
2. Sweta Prasad : Backend Development
3. Mrunali Sawant : Frontend Development
---
StrayHelp is a smart digital platform designed to transform the way stray animal rescues are managed. As a product, it empowers citizens to become active participants in animal welfare by enabling them to instantly report stray animals through photos and location details.

Built-in AI capabilities verify the animal type, evaluate the severity of visible wounds, and identify the breed, ensuring NGOs receive accurate, real-time alerts within their operational zones. NGOs and rescue teams can then respond faster, update the rescue status, and coordinate care seamlessly.

By integrating reporting, AI verification, and NGO response into one streamlined system, StrayHelp reduces delays, improves rescue efficiency, and ensures stray animals get the timely help they deserve.
