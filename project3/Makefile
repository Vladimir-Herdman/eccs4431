#Settings
TARGET_EXEC := main
TARGET_DIR := bin
BUILD_DIR := build
SRC_DIRS := src

SRC := $(shell find $(SRC_DIRS) -name '*.c')
LEXER := $(shell find $(SRC_DIRS) -name '*.l') 
PARSER := $(shell find $(SRC_DIRS) -name '*.y') 
OBJS := $(SRC:%=$(BUILD_DIR)/%.o)
DEPS := $(OBJS:.o=.d)

INC_DIRS := $(shell find $(SRC_DIRS) -type d)
INC_FLAGS := $(addprefix -I,$(INC_DIRS))

CC := clang
CFLAGS := $(INC_FLAGS) -MMD -MP -std=c23 -O3 -Wall -Wextra
LDLIBS :=
LDFLAGS :=
CDEFS :=

#Colors
ifndef VIM
	RED := \033[38;2;255;0;0m
	YELLOW := \033[38;2;255;255;0m
	GREEN := \033[38;2;21;204;4m
	NC := \033[0m
endif

#Building
$(TARGET_DIR)/$(TARGET_EXEC): $(OBJS) $(LEXER) $(PARSER)
	@mkdir -p $(dir $@)
	@$(CC) $(OBJS) -o $(TARGET_DIR)/$(TARGET_EXEC) $(LDFLAGS) $(LDLIBS) && \
		printf '\n  $(GREEN)Compiled binary$(NC): %s\n' $@

$(PARSER): src/Parser.y src/Lexer.c
	bison $(PARSER)

$(LEXER): src/Lexer.l
	@flex $(LEXER)

$(BUILD_DIR)/%.c.o: %.c
	@mkdir -p $(dir $@)
	@printf '  $(YELLOW)Compiling$(NC): %s\n' $@
	@$(CC) $(CFLAGS) $(CDEFS) -c $< -o $@

#Commands
.PHONY: clean run
clean: 
	@printf '  $(RED)rm -r$(NC) %s %s\n' $(BUILD_DIR)/ $(TARGET_DIR)/
	@rm -r build/ bin/ src/Parser.{c,h} src/Lexer.{c,h} 2>/dev/null || true

run: $(TARGET_DIR)/$(TARGET_EXEC)
	@./$(TARGET_DIR)/$(TARGET_EXEC)

-include $(DEPS)
