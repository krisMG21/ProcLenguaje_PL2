// Generated from c:/Users/ruben/Desktop/Uni/4/Lenguaje/ProcLenguaje_PL2/src/antlr_files/Basic.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class BasicParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, LET=12, PRINT=13, INPUT=14, IF=15, ELSE=16, FOR=17, 
		TO=18, NEXT=19, WHILE=20, REPEAT=21, UNTIL=22, CONTINUE=23, EXIT=24, END=25, 
		THEN=26, MOD=27, VAL=28, LEN=29, ISNAN=30, ID=31, NUMBER=32, STRING_LITERAL=33, 
		NEWLINE=34, COMMENT=35, WS=36;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_letStmt = 2, RULE_opStmt = 3, 
		RULE_printStmt = 4, RULE_inputStmt = 5, RULE_ifStmt = 6, RULE_forStmt = 7, 
		RULE_whileStmt = 8, RULE_repeatStmt = 9, RULE_keyStmt = 10, RULE_condition = 11, 
		RULE_comparisonOp = 12, RULE_expression = 13, RULE_op = 14, RULE_functionCall = 15;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "letStmt", "opStmt", "printStmt", "inputStmt", 
			"ifStmt", "forStmt", "whileStmt", "repeatStmt", "keyStmt", "condition", 
			"comparisonOp", "expression", "op", "functionCall"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "'<'", "'>'", "'<='", "'>='", "'('", "')'", "'+'", "'-'", 
			"'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"LET", "PRINT", "INPUT", "IF", "ELSE", "FOR", "TO", "NEXT", "WHILE", 
			"REPEAT", "UNTIL", "CONTINUE", "EXIT", "END", "THEN", "MOD", "VAL", "LEN", 
			"ISNAN", "ID", "NUMBER", "STRING_LITERAL", "NEWLINE", "COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Basic.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BasicParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(BasicParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(BasicParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(BasicParser.NEWLINE, i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(32);
					statement();
					setState(34); 
					_errHandler.sync(this);
					_la = _input.LA(1);
					do {
						{
						{
						setState(33);
						match(NEWLINE);
						}
						}
						setState(36); 
						_errHandler.sync(this);
						_la = _input.LA(1);
					} while ( _la==NEWLINE );
					}
					} 
				}
				setState(42);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			}
			setState(44);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2175987712L) != 0)) {
				{
				setState(43);
				statement();
				}
			}

			setState(46);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public LetStmtContext letStmt() {
			return getRuleContext(LetStmtContext.class,0);
		}
		public OpStmtContext opStmt() {
			return getRuleContext(OpStmtContext.class,0);
		}
		public PrintStmtContext printStmt() {
			return getRuleContext(PrintStmtContext.class,0);
		}
		public InputStmtContext inputStmt() {
			return getRuleContext(InputStmtContext.class,0);
		}
		public IfStmtContext ifStmt() {
			return getRuleContext(IfStmtContext.class,0);
		}
		public ForStmtContext forStmt() {
			return getRuleContext(ForStmtContext.class,0);
		}
		public WhileStmtContext whileStmt() {
			return getRuleContext(WhileStmtContext.class,0);
		}
		public RepeatStmtContext repeatStmt() {
			return getRuleContext(RepeatStmtContext.class,0);
		}
		public KeyStmtContext keyStmt() {
			return getRuleContext(KeyStmtContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(57);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LET:
				enterOuterAlt(_localctx, 1);
				{
				setState(48);
				letStmt();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(49);
				opStmt();
				}
				break;
			case PRINT:
				enterOuterAlt(_localctx, 3);
				{
				setState(50);
				printStmt();
				}
				break;
			case INPUT:
				enterOuterAlt(_localctx, 4);
				{
				setState(51);
				inputStmt();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 5);
				{
				setState(52);
				ifStmt();
				}
				break;
			case FOR:
				enterOuterAlt(_localctx, 6);
				{
				setState(53);
				forStmt();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 7);
				{
				setState(54);
				whileStmt();
				}
				break;
			case REPEAT:
				enterOuterAlt(_localctx, 8);
				{
				setState(55);
				repeatStmt();
				}
				break;
			case CONTINUE:
			case EXIT:
				enterOuterAlt(_localctx, 9);
				{
				setState(56);
				keyStmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LetStmtContext extends ParserRuleContext {
		public TerminalNode LET() { return getToken(BasicParser.LET, 0); }
		public TerminalNode ID() { return getToken(BasicParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LetStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letStmt; }
	}

	public final LetStmtContext letStmt() throws RecognitionException {
		LetStmtContext _localctx = new LetStmtContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_letStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(LET);
			setState(60);
			match(ID);
			setState(61);
			match(T__0);
			setState(62);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpStmtContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BasicParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public OpStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opStmt; }
	}

	public final OpStmtContext opStmt() throws RecognitionException {
		OpStmtContext _localctx = new OpStmtContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_opStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(ID);
			setState(65);
			match(T__0);
			setState(66);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintStmtContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(BasicParser.PRINT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public PrintStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printStmt; }
	}

	public final PrintStmtContext printStmt() throws RecognitionException {
		PrintStmtContext _localctx = new PrintStmtContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_printStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(PRINT);
			setState(69);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InputStmtContext extends ParserRuleContext {
		public TerminalNode INPUT() { return getToken(BasicParser.INPUT, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(BasicParser.STRING_LITERAL, 0); }
		public TerminalNode ID() { return getToken(BasicParser.ID, 0); }
		public InputStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inputStmt; }
	}

	public final InputStmtContext inputStmt() throws RecognitionException {
		InputStmtContext _localctx = new InputStmtContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_inputStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			match(INPUT);
			setState(72);
			match(STRING_LITERAL);
			setState(73);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(BasicParser.IF, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public TerminalNode THEN() { return getToken(BasicParser.THEN, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(BasicParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(BasicParser.NEWLINE, i);
		}
		public TerminalNode END() { return getToken(BasicParser.END, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(BasicParser.ELSE, 0); }
		public IfStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStmt; }
	}

	public final IfStmtContext ifStmt() throws RecognitionException {
		IfStmtContext _localctx = new IfStmtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_ifStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(IF);
			setState(76);
			condition();
			setState(77);
			match(THEN);
			setState(78);
			match(NEWLINE);
			setState(84);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2175987712L) != 0)) {
				{
				{
				setState(79);
				statement();
				setState(80);
				match(NEWLINE);
				}
				}
				setState(86);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(87);
				match(ELSE);
				setState(88);
				match(NEWLINE);
				setState(94);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2175987712L) != 0)) {
					{
					{
					setState(89);
					statement();
					setState(90);
					match(NEWLINE);
					}
					}
					setState(96);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(99);
			match(END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForStmtContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(BasicParser.FOR, 0); }
		public TerminalNode ID() { return getToken(BasicParser.ID, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode TO() { return getToken(BasicParser.TO, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(BasicParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(BasicParser.NEWLINE, i);
		}
		public TerminalNode NEXT() { return getToken(BasicParser.NEXT, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ForStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStmt; }
	}

	public final ForStmtContext forStmt() throws RecognitionException {
		ForStmtContext _localctx = new ForStmtContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_forStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			match(FOR);
			setState(102);
			match(ID);
			setState(103);
			match(T__0);
			setState(104);
			expression(0);
			setState(105);
			match(TO);
			setState(106);
			expression(0);
			setState(107);
			match(NEWLINE);
			setState(113);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2175987712L) != 0)) {
				{
				{
				setState(108);
				statement();
				setState(109);
				match(NEWLINE);
				}
				}
				setState(115);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(116);
			match(NEXT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStmtContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(BasicParser.WHILE, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(BasicParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(BasicParser.NEWLINE, i);
		}
		public TerminalNode END() { return getToken(BasicParser.END, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public WhileStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStmt; }
	}

	public final WhileStmtContext whileStmt() throws RecognitionException {
		WhileStmtContext _localctx = new WhileStmtContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_whileStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			match(WHILE);
			setState(119);
			condition();
			setState(120);
			match(NEWLINE);
			setState(126);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2175987712L) != 0)) {
				{
				{
				setState(121);
				statement();
				setState(122);
				match(NEWLINE);
				}
				}
				setState(128);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(129);
			match(END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RepeatStmtContext extends ParserRuleContext {
		public TerminalNode REPEAT() { return getToken(BasicParser.REPEAT, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(BasicParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(BasicParser.NEWLINE, i);
		}
		public TerminalNode UNTIL() { return getToken(BasicParser.UNTIL, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public RepeatStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repeatStmt; }
	}

	public final RepeatStmtContext repeatStmt() throws RecognitionException {
		RepeatStmtContext _localctx = new RepeatStmtContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_repeatStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			match(REPEAT);
			setState(132);
			match(NEWLINE);
			setState(138);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2175987712L) != 0)) {
				{
				{
				setState(133);
				statement();
				setState(134);
				match(NEWLINE);
				}
				}
				setState(140);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(141);
			match(UNTIL);
			setState(142);
			condition();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class KeyStmtContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(BasicParser.CONTINUE, 0); }
		public TerminalNode EXIT() { return getToken(BasicParser.EXIT, 0); }
		public KeyStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keyStmt; }
	}

	public final KeyStmtContext keyStmt() throws RecognitionException {
		KeyStmtContext _localctx = new KeyStmtContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_keyStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			_la = _input.LA(1);
			if ( !(_la==CONTINUE || _la==EXIT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ComparisonOpContext comparisonOp() {
			return getRuleContext(ComparisonOpContext.class,0);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_condition);
		try {
			setState(151);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(146);
				expression(0);
				setState(147);
				comparisonOp();
				setState(148);
				expression(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(150);
				expression(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonOpContext extends ParserRuleContext {
		public ComparisonOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparisonOp; }
	}

	public final ComparisonOpContext comparisonOp() throws RecognitionException {
		ComparisonOpContext _localctx = new ComparisonOpContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_comparisonOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 62L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public TerminalNode NUMBER() { return getToken(BasicParser.NUMBER, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(BasicParser.STRING_LITERAL, 0); }
		public TerminalNode ID() { return getToken(BasicParser.ID, 0); }
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(164);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__5:
				{
				setState(156);
				match(T__5);
				setState(157);
				expression(0);
				setState(158);
				match(T__6);
				}
				break;
			case VAL:
			case LEN:
			case ISNAN:
				{
				setState(160);
				functionCall();
				}
				break;
			case NUMBER:
				{
				setState(161);
				match(NUMBER);
				}
				break;
			case STRING_LITERAL:
				{
				setState(162);
				match(STRING_LITERAL);
				}
				break;
			case ID:
				{
				setState(163);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(172);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExpressionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression);
					setState(166);
					if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
					setState(167);
					op();
					setState(168);
					expression(7);
					}
					} 
				}
				setState(174);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpContext extends ParserRuleContext {
		public TerminalNode MOD() { return getToken(BasicParser.MOD, 0); }
		public OpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op; }
	}

	public final OpContext op() throws RecognitionException {
		OpContext _localctx = new OpContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 134221568L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallContext extends ParserRuleContext {
		public TerminalNode VAL() { return getToken(BasicParser.VAL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode LEN() { return getToken(BasicParser.LEN, 0); }
		public TerminalNode ISNAN() { return getToken(BasicParser.ISNAN, 0); }
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_functionCall);
		try {
			setState(192);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(177);
				match(VAL);
				setState(178);
				match(T__5);
				setState(179);
				expression(0);
				setState(180);
				match(T__6);
				}
				break;
			case LEN:
				enterOuterAlt(_localctx, 2);
				{
				setState(182);
				match(LEN);
				setState(183);
				match(T__5);
				setState(184);
				expression(0);
				setState(185);
				match(T__6);
				}
				break;
			case ISNAN:
				enterOuterAlt(_localctx, 3);
				{
				setState(187);
				match(ISNAN);
				setState(188);
				match(T__5);
				setState(189);
				expression(0);
				setState(190);
				match(T__6);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 13:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001$\u00c3\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0001\u0000\u0001\u0000\u0004\u0000#\b\u0000\u000b\u0000\f\u0000$\u0005"+
		"\u0000\'\b\u0000\n\u0000\f\u0000*\t\u0000\u0001\u0000\u0003\u0000-\b\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		":\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0005\u0006S\b\u0006\n\u0006\f\u0006V\t\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006]\b\u0006\n\u0006\f\u0006"+
		"`\t\u0006\u0003\u0006b\b\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0005\u0007p\b\u0007\n\u0007\f\u0007s\t"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\b\u0005\b}\b\b\n\b\f\b\u0080\t\b\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0005\t\u0089\b\t\n\t\f\t\u008c\t\t\u0001\t"+
		"\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0003\u000b\u0098\b\u000b\u0001\f\u0001\f\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u00a5"+
		"\b\r\u0001\r\u0001\r\u0001\r\u0001\r\u0005\r\u00ab\b\r\n\r\f\r\u00ae\t"+
		"\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f"+
		"\u00c1\b\u000f\u0001\u000f\u0000\u0001\u001a\u0010\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e\u0000\u0003"+
		"\u0001\u0000\u0017\u0018\u0001\u0000\u0001\u0005\u0002\u0000\b\u000b\u001b"+
		"\u001b\u00cb\u0000(\u0001\u0000\u0000\u0000\u00029\u0001\u0000\u0000\u0000"+
		"\u0004;\u0001\u0000\u0000\u0000\u0006@\u0001\u0000\u0000\u0000\bD\u0001"+
		"\u0000\u0000\u0000\nG\u0001\u0000\u0000\u0000\fK\u0001\u0000\u0000\u0000"+
		"\u000ee\u0001\u0000\u0000\u0000\u0010v\u0001\u0000\u0000\u0000\u0012\u0083"+
		"\u0001\u0000\u0000\u0000\u0014\u0090\u0001\u0000\u0000\u0000\u0016\u0097"+
		"\u0001\u0000\u0000\u0000\u0018\u0099\u0001\u0000\u0000\u0000\u001a\u00a4"+
		"\u0001\u0000\u0000\u0000\u001c\u00af\u0001\u0000\u0000\u0000\u001e\u00c0"+
		"\u0001\u0000\u0000\u0000 \"\u0003\u0002\u0001\u0000!#\u0005\"\u0000\u0000"+
		"\"!\u0001\u0000\u0000\u0000#$\u0001\u0000\u0000\u0000$\"\u0001\u0000\u0000"+
		"\u0000$%\u0001\u0000\u0000\u0000%\'\u0001\u0000\u0000\u0000& \u0001\u0000"+
		"\u0000\u0000\'*\u0001\u0000\u0000\u0000(&\u0001\u0000\u0000\u0000()\u0001"+
		"\u0000\u0000\u0000),\u0001\u0000\u0000\u0000*(\u0001\u0000\u0000\u0000"+
		"+-\u0003\u0002\u0001\u0000,+\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000"+
		"\u0000-.\u0001\u0000\u0000\u0000./\u0005\u0000\u0000\u0001/\u0001\u0001"+
		"\u0000\u0000\u00000:\u0003\u0004\u0002\u00001:\u0003\u0006\u0003\u0000"+
		"2:\u0003\b\u0004\u00003:\u0003\n\u0005\u00004:\u0003\f\u0006\u00005:\u0003"+
		"\u000e\u0007\u00006:\u0003\u0010\b\u00007:\u0003\u0012\t\u00008:\u0003"+
		"\u0014\n\u000090\u0001\u0000\u0000\u000091\u0001\u0000\u0000\u000092\u0001"+
		"\u0000\u0000\u000093\u0001\u0000\u0000\u000094\u0001\u0000\u0000\u0000"+
		"95\u0001\u0000\u0000\u000096\u0001\u0000\u0000\u000097\u0001\u0000\u0000"+
		"\u000098\u0001\u0000\u0000\u0000:\u0003\u0001\u0000\u0000\u0000;<\u0005"+
		"\f\u0000\u0000<=\u0005\u001f\u0000\u0000=>\u0005\u0001\u0000\u0000>?\u0003"+
		"\u001a\r\u0000?\u0005\u0001\u0000\u0000\u0000@A\u0005\u001f\u0000\u0000"+
		"AB\u0005\u0001\u0000\u0000BC\u0003\u001a\r\u0000C\u0007\u0001\u0000\u0000"+
		"\u0000DE\u0005\r\u0000\u0000EF\u0003\u001a\r\u0000F\t\u0001\u0000\u0000"+
		"\u0000GH\u0005\u000e\u0000\u0000HI\u0005!\u0000\u0000IJ\u0005\u001f\u0000"+
		"\u0000J\u000b\u0001\u0000\u0000\u0000KL\u0005\u000f\u0000\u0000LM\u0003"+
		"\u0016\u000b\u0000MN\u0005\u001a\u0000\u0000NT\u0005\"\u0000\u0000OP\u0003"+
		"\u0002\u0001\u0000PQ\u0005\"\u0000\u0000QS\u0001\u0000\u0000\u0000RO\u0001"+
		"\u0000\u0000\u0000SV\u0001\u0000\u0000\u0000TR\u0001\u0000\u0000\u0000"+
		"TU\u0001\u0000\u0000\u0000Ua\u0001\u0000\u0000\u0000VT\u0001\u0000\u0000"+
		"\u0000WX\u0005\u0010\u0000\u0000X^\u0005\"\u0000\u0000YZ\u0003\u0002\u0001"+
		"\u0000Z[\u0005\"\u0000\u0000[]\u0001\u0000\u0000\u0000\\Y\u0001\u0000"+
		"\u0000\u0000]`\u0001\u0000\u0000\u0000^\\\u0001\u0000\u0000\u0000^_\u0001"+
		"\u0000\u0000\u0000_b\u0001\u0000\u0000\u0000`^\u0001\u0000\u0000\u0000"+
		"aW\u0001\u0000\u0000\u0000ab\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000"+
		"\u0000cd\u0005\u0019\u0000\u0000d\r\u0001\u0000\u0000\u0000ef\u0005\u0011"+
		"\u0000\u0000fg\u0005\u001f\u0000\u0000gh\u0005\u0001\u0000\u0000hi\u0003"+
		"\u001a\r\u0000ij\u0005\u0012\u0000\u0000jk\u0003\u001a\r\u0000kq\u0005"+
		"\"\u0000\u0000lm\u0003\u0002\u0001\u0000mn\u0005\"\u0000\u0000np\u0001"+
		"\u0000\u0000\u0000ol\u0001\u0000\u0000\u0000ps\u0001\u0000\u0000\u0000"+
		"qo\u0001\u0000\u0000\u0000qr\u0001\u0000\u0000\u0000rt\u0001\u0000\u0000"+
		"\u0000sq\u0001\u0000\u0000\u0000tu\u0005\u0013\u0000\u0000u\u000f\u0001"+
		"\u0000\u0000\u0000vw\u0005\u0014\u0000\u0000wx\u0003\u0016\u000b\u0000"+
		"x~\u0005\"\u0000\u0000yz\u0003\u0002\u0001\u0000z{\u0005\"\u0000\u0000"+
		"{}\u0001\u0000\u0000\u0000|y\u0001\u0000\u0000\u0000}\u0080\u0001\u0000"+
		"\u0000\u0000~|\u0001\u0000\u0000\u0000~\u007f\u0001\u0000\u0000\u0000"+
		"\u007f\u0081\u0001\u0000\u0000\u0000\u0080~\u0001\u0000\u0000\u0000\u0081"+
		"\u0082\u0005\u0019\u0000\u0000\u0082\u0011\u0001\u0000\u0000\u0000\u0083"+
		"\u0084\u0005\u0015\u0000\u0000\u0084\u008a\u0005\"\u0000\u0000\u0085\u0086"+
		"\u0003\u0002\u0001\u0000\u0086\u0087\u0005\"\u0000\u0000\u0087\u0089\u0001"+
		"\u0000\u0000\u0000\u0088\u0085\u0001\u0000\u0000\u0000\u0089\u008c\u0001"+
		"\u0000\u0000\u0000\u008a\u0088\u0001\u0000\u0000\u0000\u008a\u008b\u0001"+
		"\u0000\u0000\u0000\u008b\u008d\u0001\u0000\u0000\u0000\u008c\u008a\u0001"+
		"\u0000\u0000\u0000\u008d\u008e\u0005\u0016\u0000\u0000\u008e\u008f\u0003"+
		"\u0016\u000b\u0000\u008f\u0013\u0001\u0000\u0000\u0000\u0090\u0091\u0007"+
		"\u0000\u0000\u0000\u0091\u0015\u0001\u0000\u0000\u0000\u0092\u0093\u0003"+
		"\u001a\r\u0000\u0093\u0094\u0003\u0018\f\u0000\u0094\u0095\u0003\u001a"+
		"\r\u0000\u0095\u0098\u0001\u0000\u0000\u0000\u0096\u0098\u0003\u001a\r"+
		"\u0000\u0097\u0092\u0001\u0000\u0000\u0000\u0097\u0096\u0001\u0000\u0000"+
		"\u0000\u0098\u0017\u0001\u0000\u0000\u0000\u0099\u009a\u0007\u0001\u0000"+
		"\u0000\u009a\u0019\u0001\u0000\u0000\u0000\u009b\u009c\u0006\r\uffff\uffff"+
		"\u0000\u009c\u009d\u0005\u0006\u0000\u0000\u009d\u009e\u0003\u001a\r\u0000"+
		"\u009e\u009f\u0005\u0007\u0000\u0000\u009f\u00a5\u0001\u0000\u0000\u0000"+
		"\u00a0\u00a5\u0003\u001e\u000f\u0000\u00a1\u00a5\u0005 \u0000\u0000\u00a2"+
		"\u00a5\u0005!\u0000\u0000\u00a3\u00a5\u0005\u001f\u0000\u0000\u00a4\u009b"+
		"\u0001\u0000\u0000\u0000\u00a4\u00a0\u0001\u0000\u0000\u0000\u00a4\u00a1"+
		"\u0001\u0000\u0000\u0000\u00a4\u00a2\u0001\u0000\u0000\u0000\u00a4\u00a3"+
		"\u0001\u0000\u0000\u0000\u00a5\u00ac\u0001\u0000\u0000\u0000\u00a6\u00a7"+
		"\n\u0006\u0000\u0000\u00a7\u00a8\u0003\u001c\u000e\u0000\u00a8\u00a9\u0003"+
		"\u001a\r\u0007\u00a9\u00ab\u0001\u0000\u0000\u0000\u00aa\u00a6\u0001\u0000"+
		"\u0000\u0000\u00ab\u00ae\u0001\u0000\u0000\u0000\u00ac\u00aa\u0001\u0000"+
		"\u0000\u0000\u00ac\u00ad\u0001\u0000\u0000\u0000\u00ad\u001b\u0001\u0000"+
		"\u0000\u0000\u00ae\u00ac\u0001\u0000\u0000\u0000\u00af\u00b0\u0007\u0002"+
		"\u0000\u0000\u00b0\u001d\u0001\u0000\u0000\u0000\u00b1\u00b2\u0005\u001c"+
		"\u0000\u0000\u00b2\u00b3\u0005\u0006\u0000\u0000\u00b3\u00b4\u0003\u001a"+
		"\r\u0000\u00b4\u00b5\u0005\u0007\u0000\u0000\u00b5\u00c1\u0001\u0000\u0000"+
		"\u0000\u00b6\u00b7\u0005\u001d\u0000\u0000\u00b7\u00b8\u0005\u0006\u0000"+
		"\u0000\u00b8\u00b9\u0003\u001a\r\u0000\u00b9\u00ba\u0005\u0007\u0000\u0000"+
		"\u00ba\u00c1\u0001\u0000\u0000\u0000\u00bb\u00bc\u0005\u001e\u0000\u0000"+
		"\u00bc\u00bd\u0005\u0006\u0000\u0000\u00bd\u00be\u0003\u001a\r\u0000\u00be"+
		"\u00bf\u0005\u0007\u0000\u0000\u00bf\u00c1\u0001\u0000\u0000\u0000\u00c0"+
		"\u00b1\u0001\u0000\u0000\u0000\u00c0\u00b6\u0001\u0000\u0000\u0000\u00c0"+
		"\u00bb\u0001\u0000\u0000\u0000\u00c1\u001f\u0001\u0000\u0000\u0000\u000e"+
		"$(,9T^aq~\u008a\u0097\u00a4\u00ac\u00c0";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}