#Settings
TARGET_EXEC := main
TARGET_DIR := bin
BUILD_DIR := build
GEN_DIR := $(BUILD_DIR)/gen
SRC_DIRS := src

LEXER := $(shell find $(SRC_DIRS) -name '*.l') 
LEXERC := $(patsubst %.l,%.c,$(patsubst $(SRC_DIRS)/%,$(GEN_DIR)/%,$(LEXER)))
PARSER := $(shell find $(SRC_DIRS) -name '*.y') 
PARSERC := $(patsubst %.y,%.c,$(patsubst $(SRC_DIRS)/%,$(GEN_DIR)/%,$(PARSER)))

SRC := $(shell find $(SRC_DIRS) -name '*.c') $(LEXERC) $(PARSERC)
OBJS := $(SRC:%=$(BUILD_DIR)/%.o)
DEPS := $(OBJS:.o=.d)

INC_DIRS := $(shell find $(SRC_DIRS) -type d)
INC_FLAGS := $(addprefix -I,$(INC_DIRS)) -Ibuild/gen

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
$(TARGET_DIR)/$(TARGET_EXEC): $(PARSERC) $(LEXERC) $(OBJS)
	@mkdir -p $(dir $@)
	@$(CC) $(OBJS) -o $(TARGET_DIR)/$(TARGET_EXEC) $(LDFLAGS) $(LDLIBS) && \
		printf '\n  $(GREEN)Compiled binary$(NC): %s\n' $@

$(BUILD_DIR)/$(GEN_DIR)/%.c.o: CFLAGS += -Wno-unused-parameter -Wno-unused-function -Wno-unneeded-internal-declaration -Wno-unused-but-set-variable
$(BUILD_DIR)/%.c.o: %.c
	@mkdir -p $(dir $@)
	@printf '  $(YELLOW)Compiling$(NC): %s\n' $@
	@$(CC) $(CFLAGS) $(CDEFS) -c $< -o $@

$(PARSERC): $(PARSER) $(LEXERC)
	@mkdir -p $(GEN_DIR)
	@printf '  $(YELLOW)Generating Parser$(NC): bison %s\n' $(PARSER)
	@bison $(PARSER)
	@mv *.c *.h $(GEN_DIR)

$(LEXERC): $(LEXER)
	@mkdir -p $(GEN_DIR)
	@printf '  $(YELLOW)Generating Lexer$(NC): flex %s\n' $(LEXER)
	@flex $(LEXER)
	@mv *.c *.h $(GEN_DIR)

#Commands
.PHONY: clean language setup run
clean: 
	@printf '  $(RED)rm -r$(NC) %s %s\n' $(BUILD_DIR)/ $(TARGET_DIR)/
	@rm -r build/ bin/ 2>/dev/null || true

language: $(PARSERC) $(LEXERC)

run: $(TARGET_DIR)/$(TARGET_EXEC)
	@./$(TARGET_DIR)/$(TARGET_EXEC)

-include $(DEPS)
