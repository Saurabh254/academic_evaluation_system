import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { GetTeacher } from "@/services/teacher";
import { Teacher } from "@/types/teachers";
import {
  CalendarIcon,
  Mail,
  MapPin,
  Phone,
  School,
  User,
  BookOpen,
  Hash,
} from "lucide-react";
import { useEffect, useState } from "react";

export default function TeacherProfile() {
  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
  };
  const [teacherData, SetTeacherData] = useState<Teacher | null>(null);
  useEffect(() => {
    const call_api = async () => {
      const response = await GetTeacher();
      if (response.status == 200) {
        SetTeacherData(response.data);
      }
    };
    call_api();
  }, []);
  const InfoItem = ({
    icon,
    label,
    value,
  }: {
    icon: React.ReactNode;
    label: string;
    value: string;
  }) => (
    <div className="flex items-center space-x-2">
      {icon}
      <span className="font-semibold">{label}:</span>
      <span>{value}</span>
    </div>
  );
  if (teacherData == null) {
    return <h1>loading...</h1>;
  }
  return (
    <div className="container mx-auto p-4">
      <Card className="w-full max-w-4xl mx-auto">
        <CardHeader>
          <CardTitle className="text-2xl font-bold">Teacher Profile</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-4">
              <InfoItem
                icon={<User className="w-5 h-5 text-primary" />}
                label="Name"
                value={teacherData.name}
              />
              <InfoItem
                icon={<Mail className="w-5 h-5 text-primary" />}
                label="Email"
                value={teacherData.email}
              />
              <InfoItem
                icon={<Phone className="w-5 h-5 text-primary" />}
                label="Phone"
                value={teacherData.phone}
              />
              <InfoItem
                icon={<MapPin className="w-5 h-5 text-primary" />}
                label="Address"
                value={teacherData.address}
              />
              <InfoItem
                icon={<Hash className="w-5 h-5 text-primary" />}
                label="Teacher ID"
                value={teacherData.id}
              />
            </div>
            <div className="space-y-4">
              <InfoItem
                icon={<School className="w-5 h-5 text-primary" />}
                label="Department"
                value={teacherData.department}
              />
              <InfoItem
                icon={<BookOpen className="w-5 h-5 text-primary" />}
                label="Subject"
                value={teacherData.subject}
              />
              <InfoItem
                icon={<CalendarIcon className="w-5 h-5 text-primary" />}
                label="Date of Birth"
                value={formatDate(teacherData.date_of_birth)}
              />
              <InfoItem
                icon={<CalendarIcon className="w-5 h-5 text-primary" />}
                label="Joining Date"
                value={formatDate(teacherData.joining_date)}
              />
              <InfoItem
                icon={<CalendarIcon className="w-5 h-5 text-primary" />}
                label="Last Updated"
                value={formatDate(teacherData.updated_at)}
              />
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
