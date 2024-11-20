import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { format } from "date-fns";
import { useEffect, useState } from "react";
import { Student } from "@/types/student";
import { ListStudents } from "@/services/student";
import { Table } from "lucide-react";
import {
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "../ui/table";
import { useNavigate } from "react-router-dom";

export default function StudentList() {
  const [students, SetStudents] = useState<Student[]>([]);
  const navigate = useNavigate();
  const handleClickStudent = (id: string) => {
    return () => {
      navigate(`/teacher/student/${id}`);
    };
  };
  useEffect(() => {
    const call_api = async () => {
      const response = await ListStudents();
      if (response.status == 200) {
        SetStudents(response.data);
      }
    };
    call_api();
  }, []);
  return (
    <div className="overflow-x-auto w-full ml-24">
      <h1 className="font-bold text-center py-4 text-xl">Students List</h1>
      <table className="table">
        <thead>
          <tr>
            <th>#</th>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Semester</th>
            <th>Date of Birth</th>
            <th>Status</th>
            <th>Registered At</th>
          </tr>
        </thead>
        {/* Table Body */}
        <tbody>
          {students.map((student, index) => (
            <tr
              key={student.id}
              onClick={handleClickStudent(student.id)}
              className="hover:bg-gray-200 cursor-pointer"
            >
              <th>{index + 1}</th>
              <td>{student.name}</td>
              <td>{student.email}</td>
              <td>{student.phone}</td>
              <td>{student.semester}</td>
              <td>{new Date(student.dob).toLocaleDateString()}</td>
              <td>{student.active ? "Active" : "Inactive"}</td>
              <td>{new Date(student.created_at).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
