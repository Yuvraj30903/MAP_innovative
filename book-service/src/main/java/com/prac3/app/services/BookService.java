package com.prac3.app.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.prac3.app.entities.Book;
import com.prac3.app.repositories.BookRepo;
import java.util.List;

@Service
public class BookService {
	
	@Autowired
	private BookRepo bookRepo;
	public Book createBook(Book book)
	{ 
		return bookRepo.save(book);
	}
	public Book updateBook(Book book)
	{ 
		return bookRepo.save(book);
	}
	public boolean deleteBook(Long bookId)
	{ 
		bookRepo.deleteById(bookId);
		return true;
	}
	public Book getBook(Long bookId)
	{ 

		return  bookRepo.findById(bookId).get();
	}
	public List<Book> getAllBook()
	{ 

		return  bookRepo.findAll();
	}
	
}
