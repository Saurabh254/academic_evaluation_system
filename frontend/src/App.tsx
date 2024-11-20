import { Route, Routes } from "react-router-dom";
import React, { Suspense } from "react";
import "remixicon/fonts/remixicon.css";

// Lazy loading the components
const LoginPage = React.lazy(() => import("./components/LoginPage"));
const StudentHomePage = React.lazy(
  () => import("./components/student/HomePage")
);
const TeacherHomePage = React.lazy(
  () => import("./components/teacher/HomePage")
);

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Routes>
        <Route path="/" element={<StudentHomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/teacher/*" element={<TeacherHomePage />} />
      </Routes>
    </Suspense>
  );
}

export default App;
