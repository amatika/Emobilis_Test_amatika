package crud_application_using_java.crud_application_using_java;

import org.springframework.data.jpa.repository.JpaRepository;

import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

public interface StudentRepository extends JpaRepository<Student, Long>
{
	
}
