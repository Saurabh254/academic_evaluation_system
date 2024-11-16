import { Route, Routes } from "react-router-dom";
import LoginPage from "./components/LoginPage";
import "remixicon/fonts/remixicon.css";
import StudentHomePage from "./components/student/HomePage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<StudentHomePage />} />
      <Route path="/login" element={<LoginPage />} />
    </Routes>
  );
}

export default App;
