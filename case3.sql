
CREATE TABLE Тур (
    id INT PRIMARY KEY AUTO_INCREMENT,
    название VARCHAR(255) NOT NULL,
    описание TEXT,
    цена DECIMAL(10, 2) NOT NULL
);


CREATE TABLE Услуга (
    id INT PRIMARY KEY AUTO_INCREMENT,
    название VARCHAR(255) NOT NULL,
    описание TEXT
);


CREATE TABLE Клиент (
    id INT PRIMARY KEY AUTO_INCREMENT,
    имя VARCHAR(255) NOT NULL,
    фамилия VARCHAR(255) NOT NULL,
    контактный_номер VARCHAR(20)
);


CREATE TABLE Заказ (
    id INT PRIMARY KEY AUTO_INCREMENT,
    клиент_id INT,
    тур_id INT,
    услуга_id INT,
    дата_заказа DATE NOT NULL,
    FOREIGN KEY (клиент_id) REFERENCES Клиент(id),
    FOREIGN KEY (тур_id) REFERENCES Тур(id),
    FOREIGN KEY (услуга_id) REFERENCES Услуга(id)
);
