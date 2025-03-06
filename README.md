# CV Generator Application

A modern, minimalist CV generator application built with Vue.js that helps users create professional CVs through a structured multi-page form.

## Features

- Multi-page form with progress tracking
- Personal information collection
- Work experience management (add/remove entries)
- Education history management (add/remove entries)
- Skills input with tag-like interface
- Professional summary section
- Certifications and projects section
- PDF generation with ATS optimization
- Clean, minimalist blue-themed design

## Components Structure

### Core Components

- **CVForm.vue**: Main form container that manages navigation between pages and maintains form data
- **ProgressBar.vue**: Visual indicator of form completion progress

### Form Pages

1. **PersonalInfoPage.vue**: Collects basic personal information
2. **WorkExperiencePage.vue**: Manages multiple work experience entries
3. **EducationPage.vue**: Manages multiple education entries
4. **SkillsSummaryPage.vue**: Collects skills and professional summary
5. **CertificationsAdditionalPage.vue**: Collects certifications, projects, and additional information

### Reusable Components

- **SelectDateBox.vue**: Reusable date selection component
- **WorkExperienceBlock.vue**: Individual work experience entry
- **EducationBlock.vue**: Individual education entry

## Technical Stack

- **Frontend**: Vue.js with TypeScript
- **Styling**: Custom CSS with minimalist blue theme
- **Backend**: Flask + Python 3.10
- **AI**: Google Gemini API
- **PDF Generation**: WeasyPrint

## Security Features

- HTML sanitization
- API key protection
- Input validation
- Safe PDF generation

## Getting Started

1. Clone the repository
2. Install dependencies:
   ```
   cd frontend
   npm install
   ```
3. Run the development server:
   ```
   npm run dev
   ```

## Form Data Structure

The CV form collects the following data structure:

```javascript
{
  // Personal Info
  firstName: string,
  lastName: string,
  email: string,
  phone: string,
  location: string,
  jobTitle: string,
  
  // Work Experience
  workExperiences: [
    {
      title: string,
      company: string,
      startDate: string,
      endDate: string,
      responsibilities: string
    }
  ],
  
  // Education
  educations: [
    {
      degree: string,
      institution: string,
      graduationDate: string
    }
  ],
  
  // Skills & Summary
  skills: string[],
  summary: string,
  
  // Certifications & Additional
  certifications: [
    {
      name: string,
      organization: string,
      date: string
    }
  ],
  projects: [
    {
      name: string,
      url: string,
      description: string
    }
  ],
  linkedin: string
}
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
