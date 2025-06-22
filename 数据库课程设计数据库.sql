/*
 Navicat Premium Data Transfer

 Source Server         : y1
 Source Server Type    : MySQL
 Source Server Version : 80036
 Source Host           : localhost:3306
 Source Schema         : y3

 Target Server Type    : MySQL
 Target Server Version : 80036
 File Encoding         : 65001

 Date: 15/09/2024 18:05:23
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for check1
-- ----------------------------
DROP TABLE IF EXISTS `check1`;
CREATE TABLE `check1`  (
  `健康码` int NOT NULL,
  `灭火器` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `自动灭火喷淋装置` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `仓库管理员编号` int NOT NULL,
  PRIMARY KEY (`仓库管理员编号`) USING BTREE,
  INDEX `健康码`(`健康码` ASC) USING BTREE,
  CONSTRAINT `chtr` FOREIGN KEY (`仓库管理员编号`) REFERENCES `staff` (`仓库管理员编号`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of check1
-- ----------------------------
INSERT INTO `check1` VALUES (1, '1', '1', 1);

-- ----------------------------
-- Table structure for entry
-- ----------------------------
DROP TABLE IF EXISTS `entry`;
CREATE TABLE `entry`  (
  `入库单编号` int NOT NULL,
  `商品编号` int NULL DEFAULT NULL,
  `入库量` int NULL DEFAULT NULL,
  `总金额` double NULL DEFAULT NULL,
  `供应商编号` int NULL DEFAULT NULL,
  `入库日期` datetime NULL DEFAULT NULL,
  `仓库编号` int NULL DEFAULT NULL,
  `仓库管理员编号` int NULL DEFAULT NULL,
  PRIMARY KEY (`入库单编号`) USING BTREE,
  INDEX `staff2`(`仓库管理员编号` ASC) USING BTREE,
  INDEX `entrygoods`(`商品编号` ASC) USING BTREE,
  INDEX `entryvendor`(`供应商编号` ASC) USING BTREE,
  INDEX `entryware`(`仓库编号` ASC, `仓库管理员编号` ASC) USING BTREE,
  CONSTRAINT `entrygoods` FOREIGN KEY (`商品编号`) REFERENCES `goods` (`商品编号`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `entrystaff` FOREIGN KEY (`仓库管理员编号`) REFERENCES `staff` (`员工编号`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `entryvendor` FOREIGN KEY (`供应商编号`) REFERENCES `vendor` (`供应商编号`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `entryware` FOREIGN KEY (`仓库编号`, `仓库管理员编号`) REFERENCES `ware` (`仓库编号`, `仓库管理员编号`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of entry
-- ----------------------------
INSERT INTO `entry` VALUES (1, 1, 11, 1111, 1, '2024-06-21 17:58:28', 1, 1);
INSERT INTO `entry` VALUES (2, 2, 200, 200, 2, '2024-06-21 00:00:00', 2, 1);
INSERT INTO `entry` VALUES (3, 3, 100, 300, 2, '2024-06-23 00:00:00', 2, 1);
INSERT INTO `entry` VALUES (4, 4, 100, 200, 2, '2024-06-23 00:00:00', 3, 1);
INSERT INTO `entry` VALUES (5, 5, 200, 600, 3, '2024-06-26 00:00:00', 2, 1);
INSERT INTO `entry` VALUES (6, 6, 100, 400, 2, '2024-06-26 00:00:00', 4, 1);

-- ----------------------------
-- Table structure for exist
-- ----------------------------
DROP TABLE IF EXISTS `exist`;
CREATE TABLE `exist`  (
  `出库单编号` int NOT NULL,
  `商品编号` int NULL DEFAULT NULL,
  `出库量` int NULL DEFAULT NULL,
  `总金额` double NULL DEFAULT NULL,
  `出库日期` datetime NULL DEFAULT NULL,
  `仓库管理员编号` int NULL DEFAULT NULL,
  `仓库编号` int NULL DEFAULT NULL,
  `员工编号` int NULL DEFAULT NULL,
  PRIMARY KEY (`出库单编号`) USING BTREE,
  INDEX `staff1`(`仓库管理员编号` ASC) USING BTREE,
  INDEX `exgo`(`商品编号` ASC) USING BTREE,
  INDEX `exst`(`员工编号` ASC) USING BTREE,
  INDEX `exwa`(`仓库管理员编号` ASC, `仓库编号` ASC) USING BTREE,
  CONSTRAINT `exgo` FOREIGN KEY (`商品编号`) REFERENCES `goods` (`商品编号`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `exst` FOREIGN KEY (`员工编号`) REFERENCES `staff` (`员工编号`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `exwa` FOREIGN KEY (`仓库管理员编号`, `仓库编号`) REFERENCES `ware` (`仓库编号`, `仓库管理员编号`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of exist
-- ----------------------------

-- ----------------------------
-- Table structure for goods
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods`  (
  `商品编号` int NOT NULL,
  `商品名称` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `规格型号` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `销售价格` decimal(10, 2) NULL DEFAULT NULL,
  `进货价格` decimal(10, 2) NULL DEFAULT NULL,
  `库存量` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `销量` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `计划库存量` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `供应商编号` int NULL DEFAULT NULL,
  `入库单号` int NULL DEFAULT NULL,
  PRIMARY KEY (`商品编号`) USING BTREE,
  INDEX `goodsentry`(`入库单号` ASC) USING BTREE,
  INDEX `goodsven`(`供应商编号` ASC) USING BTREE,
  CONSTRAINT `goodsven` FOREIGN KEY (`供应商编号`) REFERENCES `vendor` (`供应商编号`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO `goods` VALUES (1, '苹果', '水果', 3.00, 1.00, '200', '200', '300', 1, 1);
INSERT INTO `goods` VALUES (2, '西瓜', '水果', 2.00, 1.00, '200', '200', '200', 2, 2);
INSERT INTO `goods` VALUES (3, '香蕉', '水果', 3.00, 2.00, '100', '100', '100', 2, 3);
INSERT INTO `goods` VALUES (4, '葡萄', '水果', 2.00, 1.00, '100', '100', '100', 2, 4);
INSERT INTO `goods` VALUES (5, '橙子', '水果', 4.00, 2.00, '200', '200', '200', 3, 5);
INSERT INTO `goods` VALUES (6, '菠萝', '水果', 4.00, 1.00, '100', '100', '100', 2, 6);

-- ----------------------------
-- Table structure for infer
-- ----------------------------
DROP TABLE IF EXISTS `infer`;
CREATE TABLE `infer`  (
  `交易流水号` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `商品编号` int NULL DEFAULT NULL,
  `退货数量` int NULL DEFAULT NULL,
  `退款金额` double NULL DEFAULT NULL,
  `退货日期` datetime NULL DEFAULT NULL,
  INDEX `交易流水号`(`交易流水号` ASC) USING BTREE,
  INDEX `infergo`(`商品编号` ASC) USING BTREE,
  CONSTRAINT `infergo` FOREIGN KEY (`商品编号`) REFERENCES `trade` (`商品编号`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `intr` FOREIGN KEY (`交易流水号`) REFERENCES `trade` (`交易流水号`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of infer
-- ----------------------------
INSERT INTO `infer` VALUES ('100002', 2, 20, 40, '2024-06-21 00:00:00');
INSERT INTO `infer` VALUES ('100003', 3, 10, 30, '2024-06-23 00:00:00');
INSERT INTO `infer` VALUES ('100004', 3, 10, 30, '2024-06-25 00:00:00');
INSERT INTO `infer` VALUES ('100005', 1, 10, 30, '2024-06-26 00:00:00');

-- ----------------------------
-- Table structure for member
-- ----------------------------
DROP TABLE IF EXISTS `member`;
CREATE TABLE `member`  (
  `会员卡卡号` int NOT NULL,
  `会员姓名` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `性别` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `电话` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `注册日期` date NULL DEFAULT NULL,
  `累计金额` double NULL DEFAULT 0,
  `余额` double NULL DEFAULT 0,
  `会员密码` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`会员卡卡号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of member
-- ----------------------------
INSERT INTO `member` VALUES (1, '1', '男', '1', '2024-06-17', 111, 1111, '111');
INSERT INTO `member` VALUES (12345, NULL, NULL, NULL, NULL, 0, 0, '123');
INSERT INTO `member` VALUES (200003, '1', '男', '123', '2024-06-21', 0, 1500, '123456');
INSERT INTO `member` VALUES (200004, '2', '女', '1234', '2024-06-23', 0, 100, '123456');
INSERT INTO `member` VALUES (200005, '李四', '男', '123456', '2024-06-25', 0, 200, '123456');
INSERT INTO `member` VALUES (200006, '张三', '男', '12345', '2024-06-26', 0, 100, '123456');

-- ----------------------------
-- Table structure for staff
-- ----------------------------
DROP TABLE IF EXISTS `staff`;
CREATE TABLE `staff`  (
  `员工编号` int NOT NULL,
  `员工姓名` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `员工性别` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `员工年龄` int NULL DEFAULT NULL,
  `员工工龄` int NULL DEFAULT NULL,
  `身份证号码` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `联系电话` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `入职日期` date NULL DEFAULT NULL,
  `工资` decimal(10, 2) NULL DEFAULT NULL,
  `健康码` int NULL DEFAULT NULL,
  `仓库编号` int NULL DEFAULT NULL,
  `仓库管理员编号` int NULL DEFAULT NULL,
  PRIMARY KEY (`员工编号`) USING BTREE,
  INDEX `stck`(`健康码` ASC) USING BTREE,
  INDEX `仓库管理员编号`(`仓库管理员编号` ASC) USING BTREE,
  INDEX `stwa`(`仓库编号` ASC, `仓库管理员编号` ASC) USING BTREE,
  CONSTRAINT `stck` FOREIGN KEY (`健康码`) REFERENCES `check1` (`健康码`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `stwa` FOREIGN KEY (`仓库编号`, `仓库管理员编号`) REFERENCES `ware` (`仓库编号`, `仓库管理员编号`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of staff
-- ----------------------------
INSERT INTO `staff` VALUES (1, 'z', '男', 21, 2, '1111111', '11111', '2024-06-15', 2111.00, 1, 2, 1);
INSERT INTO `staff` VALUES (2, 'a', '男', 22, 1, '1111', '111111111', '2024-06-15', 2311.00, 1, 2, 1);
INSERT INTO `staff` VALUES (3, 'a', '女', 23, 2, '22222', '22222', '2024-06-15', 232322.00, 1, 4, 1);
INSERT INTO `staff` VALUES (4, 'a', '女', 23, 2, '222', '2222', '2024-06-15', 22222.00, 1, NULL, NULL);
INSERT INTO `staff` VALUES (5, '李四', '男', 19, 2, '132', '123456', '2003-12-12', 1000.00, 1, NULL, NULL);

-- ----------------------------
-- Table structure for trade
-- ----------------------------
DROP TABLE IF EXISTS `trade`;
CREATE TABLE `trade`  (
  `交易流水号` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `交易日期` datetime NULL DEFAULT NULL,
  `员工编号` int NULL DEFAULT NULL,
  `商品编号` int NULL DEFAULT NULL,
  `交易数量` int NULL DEFAULT NULL,
  `交易金额` double NULL DEFAULT NULL,
  `会员卡卡号` int NULL DEFAULT NULL,
  `类型` enum('purchase','infer') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`交易流水号`) USING BTREE,
  INDEX `trgo`(`商品编号` ASC) USING BTREE,
  INDEX `trme`(`会员卡卡号` ASC) USING BTREE,
  INDEX `trst`(`员工编号` ASC) USING BTREE,
  CONSTRAINT `trgo` FOREIGN KEY (`商品编号`) REFERENCES `goods` (`商品编号`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `trme` FOREIGN KEY (`会员卡卡号`) REFERENCES `member` (`会员卡卡号`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `trst` FOREIGN KEY (`员工编号`) REFERENCES `staff` (`员工编号`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of trade
-- ----------------------------
INSERT INTO `trade` VALUES ('1', '2024-06-17 00:00:00', 2, 1, 1, 1, 1, 'infer');
INSERT INTO `trade` VALUES ('100002', '2024-06-21 18:35:41', 1, 2, 20, 40, 200003, 'infer');
INSERT INTO `trade` VALUES ('100003', '2024-06-23 19:39:37', 1, 3, 10, 30, 200004, 'infer');
INSERT INTO `trade` VALUES ('100004', '2024-06-25 23:12:45', 1, 3, 10, 30, 200005, 'infer');
INSERT INTO `trade` VALUES ('100005', '2024-06-26 09:59:51', 1, 1, 10, 30, 200006, 'infer');

-- ----------------------------
-- Table structure for vendor
-- ----------------------------
DROP TABLE IF EXISTS `vendor`;
CREATE TABLE `vendor`  (
  `供应商编号` int NOT NULL,
  `供应商名称` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `联系电话` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `地址` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `开户银行` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `银行账户` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`供应商编号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of vendor
-- ----------------------------
INSERT INTO `vendor` VALUES (1, 'name1', '1234567890', '河南省郑州市', 'XX银行', 'XX账户');
INSERT INTO `vendor` VALUES (2, '2', '2', '2', '2', '2');
INSERT INTO `vendor` VALUES (3, '3', '3', '3', '3', '3');
INSERT INTO `vendor` VALUES (4, '4', '4', '4', '4', '4');
INSERT INTO `vendor` VALUES (5, '5', '5', '5', '5', '5');

-- ----------------------------
-- Table structure for ware
-- ----------------------------
DROP TABLE IF EXISTS `ware`;
CREATE TABLE `ware`  (
  `仓库编号` int NOT NULL,
  `仓库管理员编号` int NULL DEFAULT NULL,
  `仓库名称` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `仓库地址` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`仓库编号`) USING BTREE,
  INDEX `staff`(`仓库管理员编号` ASC) USING BTREE,
  INDEX `仓库编号`(`仓库编号` ASC, `仓库管理员编号` ASC) USING BTREE,
  CONSTRAINT `staff` FOREIGN KEY (`仓库管理员编号`) REFERENCES `staff` (`员工编号`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of ware
-- ----------------------------
INSERT INTO `ware` VALUES (1, 1, 'z', 'sa');
INSERT INTO `ware` VALUES (2, 1, 'a', 'as');
INSERT INTO `ware` VALUES (3, 1, 's', 'ss');
INSERT INTO `ware` VALUES (4, 1, 'f', 'ff');
INSERT INTO `ware` VALUES (5, NULL, '5', '5');

-- ----------------------------
-- Triggers structure for table entry
-- ----------------------------
DROP TRIGGER IF EXISTS `after_entry_insert`;
delimiter ;;
CREATE TRIGGER `after_entry_insert` AFTER INSERT ON `entry` FOR EACH ROW BEGIN
    -- 更新 goods 表中的入库单号
    UPDATE goods
    SET 入库单号 = NEW.入库单编号,供应商编号 = NEW.供应商编号
    WHERE 商品编号 = NEW.商品编号;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table trade
-- ----------------------------
DROP TRIGGER IF EXISTS `trade_goods_BEFORE`;
delimiter ;;
CREATE TRIGGER `trade_goods_BEFORE` BEFORE INSERT ON `trade` FOR EACH ROW BEGIN
    DECLARE 当前库存 INT;

    -- 获取当前库存
    SELECT 库存量 INTO 当前库存 FROM goods WHERE 商品编号 = NEW.商品编号;

    -- 检查是否购买并导致库存不足
    IF NEW.类型 = 'purchase' AND 当前库存 < NEW.交易数量 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '库存不足，无法完成交易';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table trade
-- ----------------------------
DROP TRIGGER IF EXISTS `before_trade_mem`;
delimiter ;;
CREATE TRIGGER `before_trade_mem` BEFORE INSERT ON `trade` FOR EACH ROW BEGIN
    DECLARE 当前余额 double;

    -- 获取当前余额
    SELECT 余额 INTO 当前余额 FROM member WHERE 会员卡卡号 = NEW.会员卡卡号;

    -- 检查是否购买并导致余额不足
    IF NEW.类型 = 'purchase' AND 当前余额 < NEW.交易金额 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '余额不足，无法完成交易';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table trade
-- ----------------------------
DROP TRIGGER IF EXISTS `tr_mem`;
delimiter ;;
CREATE TRIGGER `tr_mem` AFTER INSERT ON `trade` FOR EACH ROW BEGIN
    -- 处理购买交易
    IF NEW.类型 = 'purchase' THEN
        UPDATE member
        SET 累计金额 = 累计金额 + NEW.交易金额,
            余额 = 余额 - NEW.交易金额
        WHERE 会员卡卡号 = NEW.会员卡卡号;
    -- 处理退款交易
    ELSEIF NEW.类型 = 'infer' THEN
        UPDATE member
        SET 累计金额 = 累计金额 - NEW.交易金额,
            余额 = 余额 + NEW.交易金额
        WHERE 会员卡卡号 = NEW.会员卡卡号;
    END IF;
    END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table trade
-- ----------------------------
DROP TRIGGER IF EXISTS `trade_goods`;
delimiter ;;
CREATE TRIGGER `trade_goods` AFTER INSERT ON `trade` FOR EACH ROW BEGIN
    -- 更新 goods 表的 销量 和 库存量
    IF NEW.类型 = 'purchase' THEN
        UPDATE goods
        SET 销量 = 销量 + NEW.交易数量,
            库存量 = 库存量 - NEW.交易数量
        WHERE 商品编号 = NEW.商品编号;
    ELSEIF NEW.类型 = 'infer' THEN
        UPDATE goods
        SET 销量 = 销量 - NEW.交易数量,
            库存量 = 库存量 + NEW.交易数量
        WHERE 商品编号 = NEW.商品编号;
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table trade
-- ----------------------------
DROP TRIGGER IF EXISTS `after_trade_insert`;
delimiter ;;
CREATE TRIGGER `after_trade_insert` AFTER INSERT ON `trade` FOR EACH ROW BEGIN
    -- 检查是否为退货类型
    IF NEW.类型 = 'infer' THEN
        INSERT INTO infer (交易流水号, 商品编号, 退货数量, 退款金额, 退货日期)
        VALUES (NEW.交易流水号, NEW.商品编号, NEW.交易数量, NEW.交易金额, CURDATE());
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table trade
-- ----------------------------
DROP TRIGGER IF EXISTS `after_trade_update`;
delimiter ;;
CREATE TRIGGER `after_trade_update` AFTER UPDATE ON `trade` FOR EACH ROW BEGIN
    -- 检查是否为退货类型
    IF NEW.类型 = 'infer' THEN
        UPDATE infer
        SET 商品编号 = NEW.商品编号,
            退货数量 = NEW.交易数量,
            退款金额 = NEW.交易金额,
            退货日期 = CURDATE()
        WHERE 交易流水号 = NEW.交易流水号;
    END IF;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
