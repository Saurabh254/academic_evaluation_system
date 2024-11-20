import { Route, Routes } from "react-router-dom";
import StudentList from "./StudentList";
import StudentView from "./StudentView";
import TeacherProfile from "./TeacherProfile";

const MainView = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<TeacherProfile />}></Route>
        <Route path="/student/:id" element={<StudentView />}></Route>
        <Route path="/students" element={<StudentList />}></Route>
      </Routes>
    </>
  );
};
export default MainView;
