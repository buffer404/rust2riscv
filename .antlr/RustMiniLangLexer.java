// Generated from //wsl.localhost/Ubuntu/home/leonid/rust2riscv/RustMiniLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class RustMiniLangLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, BOOL=19, AND=20, OR=21, ASTERISK=22, SLASH=23, PLUS=24, MINUS=25, 
		ASSIGN=26, EQUAL=27, NOT_EQUAL=28, LESS=29, LESS_OR_EQUAL=30, GREATER=31, 
		GREATER_OR_EQUAL=32, NUM=33, ID=34, SPACE=35, LINE_COMMENT=36, BLOCK_COMMENT=37;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
			"T__17", "BOOL", "AND", "OR", "ASTERISK", "SLASH", "PLUS", "MINUS", "ASSIGN", 
			"EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
			"NUM", "ID", "SPACE", "LINE_COMMENT", "BLOCK_COMMENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'let'", "'mut'", "':'", "';'", "'i32'", "'bool'", 
			"'println!'", "'\"'", "'{'", "'}'", "'if'", "'else'", "'while'", "'for'", 
			"'in'", "'..'", null, "'&'", "'|'", "'*'", "'/'", "'+'", "'-'", "'='", 
			"'=='", "'!='", "'<'", "'<='", "'>'", "'>='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, "BOOL", "AND", "OR", "ASTERISK", 
			"SLASH", "PLUS", "MINUS", "ASSIGN", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", 
			"GREATER", "GREATER_OR_EQUAL", "NUM", "ID", "SPACE", "LINE_COMMENT", 
			"BLOCK_COMMENT"
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


	public RustMiniLangLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "RustMiniLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000%\u00e0\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007"+
		"!\u0002\"\u0007\"\u0002#\u0007#\u0002$\u0007$\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u0095\b\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015"+
		"\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018"+
		"\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001\u001f"+
		"\u0001 \u0004 \u00b6\b \u000b \f \u00b7\u0001!\u0001!\u0005!\u00bc\b!"+
		"\n!\f!\u00bf\t!\u0001\"\u0004\"\u00c2\b\"\u000b\"\f\"\u00c3\u0001\"\u0001"+
		"\"\u0001#\u0001#\u0001#\u0001#\u0005#\u00cc\b#\n#\f#\u00cf\t#\u0001#\u0001"+
		"#\u0001$\u0001$\u0001$\u0001$\u0005$\u00d7\b$\n$\f$\u00da\t$\u0001$\u0001"+
		"$\u0001$\u0001$\u0001$\u0001\u00d8\u0000%\u0001\u0001\u0003\u0002\u0005"+
		"\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n"+
		"\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011"+
		"#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017/\u00181\u00193\u001a5\u001b"+
		"7\u001c9\u001d;\u001e=\u001f? A!C\"E#G$I%\u0001\u0000\u0005\u0001\u0000"+
		"09\u0003\u0000AZ__az\u0004\u000009AZ__az\u0003\u0000\t\n\r\r  \u0002\u0000"+
		"\n\n\r\r\u00e5\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000"+
		"\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%"+
		"\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001"+
		"\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000"+
		"\u0000\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u0000"+
		"3\u0001\u0000\u0000\u0000\u00005\u0001\u0000\u0000\u0000\u00007\u0001"+
		"\u0000\u0000\u0000\u00009\u0001\u0000\u0000\u0000\u0000;\u0001\u0000\u0000"+
		"\u0000\u0000=\u0001\u0000\u0000\u0000\u0000?\u0001\u0000\u0000\u0000\u0000"+
		"A\u0001\u0000\u0000\u0000\u0000C\u0001\u0000\u0000\u0000\u0000E\u0001"+
		"\u0000\u0000\u0000\u0000G\u0001\u0000\u0000\u0000\u0000I\u0001\u0000\u0000"+
		"\u0000\u0001K\u0001\u0000\u0000\u0000\u0003M\u0001\u0000\u0000\u0000\u0005"+
		"O\u0001\u0000\u0000\u0000\u0007S\u0001\u0000\u0000\u0000\tW\u0001\u0000"+
		"\u0000\u0000\u000bY\u0001\u0000\u0000\u0000\r[\u0001\u0000\u0000\u0000"+
		"\u000f_\u0001\u0000\u0000\u0000\u0011d\u0001\u0000\u0000\u0000\u0013m"+
		"\u0001\u0000\u0000\u0000\u0015o\u0001\u0000\u0000\u0000\u0017q\u0001\u0000"+
		"\u0000\u0000\u0019s\u0001\u0000\u0000\u0000\u001bv\u0001\u0000\u0000\u0000"+
		"\u001d{\u0001\u0000\u0000\u0000\u001f\u0081\u0001\u0000\u0000\u0000!\u0085"+
		"\u0001\u0000\u0000\u0000#\u0088\u0001\u0000\u0000\u0000%\u0094\u0001\u0000"+
		"\u0000\u0000\'\u0096\u0001\u0000\u0000\u0000)\u0098\u0001\u0000\u0000"+
		"\u0000+\u009a\u0001\u0000\u0000\u0000-\u009c\u0001\u0000\u0000\u0000/"+
		"\u009e\u0001\u0000\u0000\u00001\u00a0\u0001\u0000\u0000\u00003\u00a2\u0001"+
		"\u0000\u0000\u00005\u00a4\u0001\u0000\u0000\u00007\u00a7\u0001\u0000\u0000"+
		"\u00009\u00aa\u0001\u0000\u0000\u0000;\u00ac\u0001\u0000\u0000\u0000="+
		"\u00af\u0001\u0000\u0000\u0000?\u00b1\u0001\u0000\u0000\u0000A\u00b5\u0001"+
		"\u0000\u0000\u0000C\u00b9\u0001\u0000\u0000\u0000E\u00c1\u0001\u0000\u0000"+
		"\u0000G\u00c7\u0001\u0000\u0000\u0000I\u00d2\u0001\u0000\u0000\u0000K"+
		"L\u0005(\u0000\u0000L\u0002\u0001\u0000\u0000\u0000MN\u0005)\u0000\u0000"+
		"N\u0004\u0001\u0000\u0000\u0000OP\u0005l\u0000\u0000PQ\u0005e\u0000\u0000"+
		"QR\u0005t\u0000\u0000R\u0006\u0001\u0000\u0000\u0000ST\u0005m\u0000\u0000"+
		"TU\u0005u\u0000\u0000UV\u0005t\u0000\u0000V\b\u0001\u0000\u0000\u0000"+
		"WX\u0005:\u0000\u0000X\n\u0001\u0000\u0000\u0000YZ\u0005;\u0000\u0000"+
		"Z\f\u0001\u0000\u0000\u0000[\\\u0005i\u0000\u0000\\]\u00053\u0000\u0000"+
		"]^\u00052\u0000\u0000^\u000e\u0001\u0000\u0000\u0000_`\u0005b\u0000\u0000"+
		"`a\u0005o\u0000\u0000ab\u0005o\u0000\u0000bc\u0005l\u0000\u0000c\u0010"+
		"\u0001\u0000\u0000\u0000de\u0005p\u0000\u0000ef\u0005r\u0000\u0000fg\u0005"+
		"i\u0000\u0000gh\u0005n\u0000\u0000hi\u0005t\u0000\u0000ij\u0005l\u0000"+
		"\u0000jk\u0005n\u0000\u0000kl\u0005!\u0000\u0000l\u0012\u0001\u0000\u0000"+
		"\u0000mn\u0005\"\u0000\u0000n\u0014\u0001\u0000\u0000\u0000op\u0005{\u0000"+
		"\u0000p\u0016\u0001\u0000\u0000\u0000qr\u0005}\u0000\u0000r\u0018\u0001"+
		"\u0000\u0000\u0000st\u0005i\u0000\u0000tu\u0005f\u0000\u0000u\u001a\u0001"+
		"\u0000\u0000\u0000vw\u0005e\u0000\u0000wx\u0005l\u0000\u0000xy\u0005s"+
		"\u0000\u0000yz\u0005e\u0000\u0000z\u001c\u0001\u0000\u0000\u0000{|\u0005"+
		"w\u0000\u0000|}\u0005h\u0000\u0000}~\u0005i\u0000\u0000~\u007f\u0005l"+
		"\u0000\u0000\u007f\u0080\u0005e\u0000\u0000\u0080\u001e\u0001\u0000\u0000"+
		"\u0000\u0081\u0082\u0005f\u0000\u0000\u0082\u0083\u0005o\u0000\u0000\u0083"+
		"\u0084\u0005r\u0000\u0000\u0084 \u0001\u0000\u0000\u0000\u0085\u0086\u0005"+
		"i\u0000\u0000\u0086\u0087\u0005n\u0000\u0000\u0087\"\u0001\u0000\u0000"+
		"\u0000\u0088\u0089\u0005.\u0000\u0000\u0089\u008a\u0005.\u0000\u0000\u008a"+
		"$\u0001\u0000\u0000\u0000\u008b\u008c\u0005t\u0000\u0000\u008c\u008d\u0005"+
		"r\u0000\u0000\u008d\u008e\u0005u\u0000\u0000\u008e\u0095\u0005e\u0000"+
		"\u0000\u008f\u0090\u0005f\u0000\u0000\u0090\u0091\u0005a\u0000\u0000\u0091"+
		"\u0092\u0005l\u0000\u0000\u0092\u0093\u0005s\u0000\u0000\u0093\u0095\u0005"+
		"e\u0000\u0000\u0094\u008b\u0001\u0000\u0000\u0000\u0094\u008f\u0001\u0000"+
		"\u0000\u0000\u0095&\u0001\u0000\u0000\u0000\u0096\u0097\u0005&\u0000\u0000"+
		"\u0097(\u0001\u0000\u0000\u0000\u0098\u0099\u0005|\u0000\u0000\u0099*"+
		"\u0001\u0000\u0000\u0000\u009a\u009b\u0005*\u0000\u0000\u009b,\u0001\u0000"+
		"\u0000\u0000\u009c\u009d\u0005/\u0000\u0000\u009d.\u0001\u0000\u0000\u0000"+
		"\u009e\u009f\u0005+\u0000\u0000\u009f0\u0001\u0000\u0000\u0000\u00a0\u00a1"+
		"\u0005-\u0000\u0000\u00a12\u0001\u0000\u0000\u0000\u00a2\u00a3\u0005="+
		"\u0000\u0000\u00a34\u0001\u0000\u0000\u0000\u00a4\u00a5\u0005=\u0000\u0000"+
		"\u00a5\u00a6\u0005=\u0000\u0000\u00a66\u0001\u0000\u0000\u0000\u00a7\u00a8"+
		"\u0005!\u0000\u0000\u00a8\u00a9\u0005=\u0000\u0000\u00a98\u0001\u0000"+
		"\u0000\u0000\u00aa\u00ab\u0005<\u0000\u0000\u00ab:\u0001\u0000\u0000\u0000"+
		"\u00ac\u00ad\u0005<\u0000\u0000\u00ad\u00ae\u0005=\u0000\u0000\u00ae<"+
		"\u0001\u0000\u0000\u0000\u00af\u00b0\u0005>\u0000\u0000\u00b0>\u0001\u0000"+
		"\u0000\u0000\u00b1\u00b2\u0005>\u0000\u0000\u00b2\u00b3\u0005=\u0000\u0000"+
		"\u00b3@\u0001\u0000\u0000\u0000\u00b4\u00b6\u0007\u0000\u0000\u0000\u00b5"+
		"\u00b4\u0001\u0000\u0000\u0000\u00b6\u00b7\u0001\u0000\u0000\u0000\u00b7"+
		"\u00b5\u0001\u0000\u0000\u0000\u00b7\u00b8\u0001\u0000\u0000\u0000\u00b8"+
		"B\u0001\u0000\u0000\u0000\u00b9\u00bd\u0007\u0001\u0000\u0000\u00ba\u00bc"+
		"\u0007\u0002\u0000\u0000\u00bb\u00ba\u0001\u0000\u0000\u0000\u00bc\u00bf"+
		"\u0001\u0000\u0000\u0000\u00bd\u00bb\u0001\u0000\u0000\u0000\u00bd\u00be"+
		"\u0001\u0000\u0000\u0000\u00beD\u0001\u0000\u0000\u0000\u00bf\u00bd\u0001"+
		"\u0000\u0000\u0000\u00c0\u00c2\u0007\u0003\u0000\u0000\u00c1\u00c0\u0001"+
		"\u0000\u0000\u0000\u00c2\u00c3\u0001\u0000\u0000\u0000\u00c3\u00c1\u0001"+
		"\u0000\u0000\u0000\u00c3\u00c4\u0001\u0000\u0000\u0000\u00c4\u00c5\u0001"+
		"\u0000\u0000\u0000\u00c5\u00c6\u0006\"\u0000\u0000\u00c6F\u0001\u0000"+
		"\u0000\u0000\u00c7\u00c8\u0005/\u0000\u0000\u00c8\u00c9\u0005/\u0000\u0000"+
		"\u00c9\u00cd\u0001\u0000\u0000\u0000\u00ca\u00cc\b\u0004\u0000\u0000\u00cb"+
		"\u00ca\u0001\u0000\u0000\u0000\u00cc\u00cf\u0001\u0000\u0000\u0000\u00cd"+
		"\u00cb\u0001\u0000\u0000\u0000\u00cd\u00ce\u0001\u0000\u0000\u0000\u00ce"+
		"\u00d0\u0001\u0000\u0000\u0000\u00cf\u00cd\u0001\u0000\u0000\u0000\u00d0"+
		"\u00d1\u0006#\u0000\u0000\u00d1H\u0001\u0000\u0000\u0000\u00d2\u00d3\u0005"+
		"/\u0000\u0000\u00d3\u00d4\u0005*\u0000\u0000\u00d4\u00d8\u0001\u0000\u0000"+
		"\u0000\u00d5\u00d7\t\u0000\u0000\u0000\u00d6\u00d5\u0001\u0000\u0000\u0000"+
		"\u00d7\u00da\u0001\u0000\u0000\u0000\u00d8\u00d9\u0001\u0000\u0000\u0000"+
		"\u00d8\u00d6\u0001\u0000\u0000\u0000\u00d9\u00db\u0001\u0000\u0000\u0000"+
		"\u00da\u00d8\u0001\u0000\u0000\u0000\u00db\u00dc\u0005*\u0000\u0000\u00dc"+
		"\u00dd\u0005/\u0000\u0000\u00dd\u00de\u0001\u0000\u0000\u0000\u00de\u00df"+
		"\u0006$\u0000\u0000\u00dfJ\u0001\u0000\u0000\u0000\u0007\u0000\u0094\u00b7"+
		"\u00bd\u00c3\u00cd\u00d8\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}