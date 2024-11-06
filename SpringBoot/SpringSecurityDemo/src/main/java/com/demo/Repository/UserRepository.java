package com.demo.Repository;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

import com.demo.Entity.User;

public interface UserRepository extends JpaRepository<User,Integer> {
Optional<User> findByEmail(String email);
}
