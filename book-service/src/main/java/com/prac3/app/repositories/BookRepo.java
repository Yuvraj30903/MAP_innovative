package com.prac3.app.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.prac3.app.entities.Book;

public interface BookRepo extends JpaRepository<Book, Long> {
	
}
