import React, { useRef, useState } from 'react';
import './App.css';
import { GrAdd } from "react-icons/gr";
import axios from 'axios';

function Home() {
  const [generatedQuestions, setGeneratedQuestions] = useState([]);
  const fileInputRef = useRef(null);
  const [fileName, setFileName] = useState('');
  const [selectedFile, setSelectedFile] = useState(null);
  const [questionType, setQuestionType] = useState('');
  const [questionCount, setQuestionCount] = useState(5);

  const handleAddClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (
      file &&
      (file.type === 'application/pdf' ||
        file.type === 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    ) {
      setFileName(file.name);
      setSelectedFile(file); // store the file for upload
      console.log('File selected:', file.name);
    } else {
      alert('Please select a valid PDF or Word (.docx) file');
    }
  };

  const handleGenerate = async () => {
    if (!selectedFile) {
      alert('Please upload a file first');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);
    formData.append('question_type', questionType);
    formData.append('question_count', questionCount);

    try {
      const response = await axios.post('http://127.0.0.1:8000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      console.log('Backend Response:', response.data);

      if (response.data.text_preview) {
        alert(`Extracted Text Preview:\n\n${response.data.text_preview}`);
      } else {
        alert('No preview text received.');
      }

      if (response.data.questions) {
        console.log('Generated Questions:', response.data.questions);
        setGeneratedQuestions(response.data.questions);
      }

    } catch (error) {
      console.error('Upload failed:', error);
      alert('Something went wrong while uploading');
    }
  };

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#0F1D3D', paddingBottom: '150px' }}>
      <div
        className='container'
        style={{
          backgroundColor: '#12234B',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          position: 'fixed',
          bottom: '100px',
          width: '75%',
          height: '70px',
          left: '50%',
          transform: 'translateX(-50%)',
          borderRadius: '33px',
          padding: '0 20px',
          color: 'white',
        }}
      >
        {/* Left side: + icon and file name or instruction text */}
        <div style={{ display: 'flex', alignItems: 'center' }}>
          <div
            onClick={handleAddClick}
            style={{
              cursor: 'pointer',
              borderRadius: '50%',
              width: '40px',
              height: '40px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              marginRight: '15px',
            }}
          >
            <GrAdd color="#12234B" size={20} />
          </div>

          {/* Show either file name or instruction text */}
          <p style={{ margin: 0, fontSize: '16px' }}>
            {fileName ? fileName : 'Upload a PDF or Word file to begin'}
          </p>
        </div>

        {/* Right side: options (only show if file is selected) */}
        {fileName && (
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <select
              value={questionType}
              onChange={(e) => setQuestionType(e.target.value)}
              style={{
                padding: '5px',
                borderRadius: '8px',
                backgroundColor: '#1A2E5C',
                border: 'none',
                outline: 'none',
              }}
            >
              <option value="" disabled>Select Question Type</option>
              <option value="mcq">MCQ</option>
              <option value="fillups">Fill-Ups</option>
              <option value="truefalse">True / False</option>
              <option value="descriptive">Descriptive</option>
            </select>
            <input
              type="number"
              min="1"
              value={questionCount}
              onChange={(e) => setQuestionCount(e.target.value)}
              style={{
                width: '60px',
                borderRadius: '8px',
                backgroundColor: '#1A2E5C',
                border: 'none',
                padding: '5px',
              }}
            />
            <button
              onClick={handleGenerate}
              style={{
                padding: '6px 12px',
                backgroundColor: '#0F1D3D',
                color: 'white',
                borderRadius: '8px',
                border: 'none',
                cursor: 'pointer',
              }}
            >
              Generate
            </button>
          </div>
        )}

        {/* Hidden file input */}
        <input
          ref={fileInputRef}
          onChange={handleFileChange}
          type="file"
          accept="application/pdf,application/vnd.openxmlformats-officedocument.wordprocessingml.document"
          style={{ display: 'none' }}
        />
      </div>

      {/* Generated Questions */}
      {generatedQuestions.length > 0 && (
        <div style={{ color: 'white', padding: '30px 50px' }}>
          <h2>Generated Questions:</h2>
          <ol>
            {generatedQuestions.map((q, index) => (
              <li key={index} style={{ marginBottom: '20px' }}>
                <p><strong>Q{index + 1}:</strong> {q.question}</p>
                {q.options && (
                  <ul>
                    {q.options.map((opt, i) => (
                      <li key={i}>{opt}</li>
                    ))}
                  </ul>
                )}
                <p><strong>Answer:</strong> {String(q.answer)}</p>
              </li>
            ))}
          </ol>
        </div>
      )}
    </div>
  );
}

export default Home;
