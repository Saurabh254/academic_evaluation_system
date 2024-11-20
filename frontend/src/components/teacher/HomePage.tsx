import { lazy } from "react";
import Main from "./Main";
const TeacherProfile = lazy(() => import("./TeacherProfile"));

export default function Home() {
  const teacherData = {
    password: "string",
    email: "user@example.com",
    date_of_birth: "2024-11-17",
    name: "string",
    joining_date: "2024-11-17",
    id: "TEACH11150",
    created_at: "2024-11-17T15:14:39.878709+00:00",
    phone: "string",
    subject: "string",
    department: "string",
    address: "string",
    updated_at: "2024-11-17T15:14:39.878711+00:00",
  };

  return <Main />;
}
