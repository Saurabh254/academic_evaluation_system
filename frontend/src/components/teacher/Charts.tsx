import { ColumnChart } from "@/common/GradeCharts";
import { StudentGrade } from "@/types/grades";

interface Charts {
  grades: StudentGrade[];
}

const Charts = ({ grades }: Charts) => {
  if (grades == null || grades.length == 0) {
    return <span className="mb-8">no grades available</span>;
  }
  return (
    <div className="flex flex-wrap justify-center gap-24">
      {grades.map((e) => {
        return (
          <ColumnChart
            student_grade={e}
            key={grades.student_id + "-" + grades.semester}
          />
        );
      })}
    </div>
  );
};

export default Charts;
