# Agent Skills — od pierwszego spotkania do własnej instrukcji

Agent Skills to sposób pakowania instrukcji i materiałów dla asystenta AI, aby mógł korzystać z nich przy konkretnych zadaniach. Nie trzeba zaczynać od programowania: najprostszy skill to folder z jednym czytelnym plikiem tekstowym.

**Jak czytać:** jeśli temat jest nowy, zacznij od pierwszej części. Jeśli znasz już prompty i narzędzia agentów, przejdź do budowy skilla. Na końcu znajdziesz historię, ograniczenia i źródła do dalszej nauki.

## Spis treści

- [1. Nie wiem jeszcze, czym są skills](#1-nie-wiem-jeszcze-czym-są-skills)
- [2. Znam podstawy — jak wygląda skill?](#2-znam-podstawy--jak-wygląda-skill)
- [3. Chcę zrozumieć więcej](#3-chcę-zrozumieć-więcej)
- [4. Gdzie pasuje to repozytorium?](#4-gdzie-pasuje-to-repozytorium)
- [5. Ograniczenia i bezpieczne korzystanie](#5-ograniczenia-i-bezpieczne-korzystanie)
- [6. Czytanie u źródła](#6-czytanie-u-źródła)

## 1. Nie wiem jeszcze, czym są skills

Wyobraź sobie nową osobę w zespole. Potrafi pisać, analizować i korzystać z komputera, ale nie zna waszego sposobu pracy. Dajesz jej **teczkę wdrożeniową**: kiedy stosować daną procedurę, kolejne kroki, przykład dobrego wyniku i listę rzeczy, których nie wolno robić. Skill pełni podobną rolę wobec agenta AI.

Agent to tutaj aplikacja wykorzystująca model AI, która może nie tylko odpowiadać, ale również wykonywać zadania przy użyciu udostępnionych narzędzi. Skill opisuje, **jak podejść do określonego rodzaju pracy**. Może na przykład pomagać rozbić dużą funkcję programu na małą zmianę, sprawdzić implementację względem wymagań albo przygotować procedurę IT.

Zamiast za każdym razem wklejać długi prompt, przechowujesz instrukcję w plikach. Możesz ją poprawiać, przeglądać zmiany i udostępniać zespołowi. Dobry skill zawiera nie tylko kroki, lecz także warunki użycia, granice zadania i sposób sprawdzenia rezultatu.

### Czym skill nie jest?

- **Nie jest treningiem modelu.** Instrukcje trafiają do kontekstu podczas pracy; samo użycie skilla nie zmienia wag modelu ani nie oznacza trwałego nauczenia go nowej umiejętności.
- **Nie jest osobnym modelem ani samodzielnym agentem.** To materiał dla aplikacji, która musi umieć go odnaleźć i wykorzystać.
- **Nie jest tym samym co narzędzie.** Narzędzie wykonuje operację, np. odczytuje plik. Skill może opisywać, kiedy i jak użyć tego narzędzia, oraz zawierać pomocniczy skrypt.
- **Nie jest MCP.** Model Context Protocol standaryzuje połączenia aplikacji AI z zewnętrznymi systemami, danymi i narzędziami; obsługuje też zasoby i prompty. Skill organizuje instrukcje i zasoby do konkretnej pracy. Mogą się uzupełniać: połączenie dostarcza dostęp, a skill opisuje procedurę korzystania z niego.

## 2. Znam podstawy — jak wygląda skill?

Według [specyfikacji Agent Skills](https://agentskills.io/specification) minimum to katalog zawierający plik `SKILL.md`. To Markdown, czyli zwykły tekst z prostym zapisem nagłówków i list, poprzedzony metadanymi YAML między liniami `---`.

Przykładowy plik `podsumowanie-spotkania/SKILL.md`:

```markdown
---
name: podsumowanie-spotkania
description: Przygotowuje podsumowanie z dostarczonych notatek. Użyj, gdy użytkownik prosi o decyzje i zadania po spotkaniu.
---

# Podsumowanie spotkania

1. Przeczytaj dostarczone notatki. Nie dopisuj nieznanych faktów.
2. Wypisz decyzje oraz zadania z osobą odpowiedzialną i terminem.
3. Jeśli brakuje osoby lub terminu, oznacz tę informację jako nieustaloną.
4. Na końcu wypisz otwarte pytania. Nie wysyłaj podsumowania samodzielnie.
```

Wymagane są `name` i `description`. Nazwa musi odpowiadać nazwie katalogu; ten przykład używa małych liter i pojedynczych myślników. Opis powinien mówić zarówno **co skill robi**, jak i **kiedy go używać**. Specyfikacja ogranicza długość nazwy do 64 znaków, a opisu do 1024.

Większa teczka może wyglądać tak:

```text
podsumowanie-spotkania/
├── SKILL.md
├── references/   # dodatkowe wskazówki i przykłady
├── assets/       # szablony wyniku
└── scripts/      # opcjonalny kod pomocniczy
```

Dodatkowe katalogi nie są obowiązkowe. Zacznij od jednej instrukcji; zasoby dodawaj wtedy, gdy rzeczywiście pomagają. Przykład powyżej nie wymaga skryptu, dostępu do poczty ani połączenia z kalendarzem.

## 3. Chcę zrozumieć więcej

### Dlaczego agent nie czyta od razu wszystkiego?

Kluczową zasadą jest **progressive disclosure**, czyli stopniowe ujawnianie szczegółów:

1. Najpierw agent otrzymuje krótkie metadane dostępnych skills — nazwę i opis.
2. Gdy zadanie pasuje, odczytuje pełny `SKILL.md`.
3. Dopiero w razie potrzeby sięga po wskazane materiały albo uruchamia pomocniczy kod, jeśli środowisko na to pozwala.

To odpowiednik przejrzenia etykiet teczek, otwarcia właściwej i przeczytania potrzebnego załącznika. Pozwala ograniczać ilość materiału w kontekście modelu. Nie oznacza jednak nieograniczonego okna kontekstowego ani gwarancji, że agent zawsze wybierze właściwą instrukcję.

Jest to wzorzec opisany w specyfikacji i artykule inżynierskim Anthropic. Konkretne aplikacje mogą różnić się wykrywaniem, ręcznym wywoływaniem, miejscem przechowywania i obsługą dodatkowych pól. **Przenośny format nie gwarantuje identycznego działania**: liczą się narzędzia, zależności, uprawnienia i implementacja klienta.

### Skąd pochodzi ten format?

[Oficjalna strona standardu](https://agentskills.io/home) wskazuje **Anthropic** jako organizację, która pierwotnie opracowała format Agent Skills. Warto rozdzielić dwa publiczne wydarzenia:

- **16 października 2025 r. — publiczne uruchomienie Agent Skills w Claude.** [Informacje o wydaniach Claude Platform](https://platform.claude.com/docs/en/release-notes/overview#october-16-2025) zawierają pod tą datą wpis „We've launched Agent Skills”, opis folderów i pierwszej wersji funkcji. Towarzyszyło mu [ogłoszenie produktowe](https://claude.com/resources/articles/skills).
- **18 grudnia 2025 r. — publikacja Agent Skills jako otwartego standardu.** Datująca tę zmianę aktualizacja znajduje się na początku ogłoszenia i [artykułu inżynierskiego](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).

To daty publicznego udostępnienia i ogłoszenia standardu, **nie ustalona data pierwszego wewnętrznego pomysłu lub prototypu**. Źródła te nie uzasadniają przypisania Anthropic wynalezienia całej idei wielokrotnie używanych instrukcji dla agentów.

Artykuł inżynierski wymienia jako swoich autorów **Barry'ego Zhanga, Keitha Lazukę i Mahesha Muraga**, a podziękowania obejmują szerszy zespół Anthropic. Autorstwo tekstu nie jest dowodem, że jedna z tych osób samodzielnie „wynalazła skills”.

## 4. Gdzie pasuje to repozytorium?

[Repozytorium `voytas75/skills`](README.md) to praktyczny zbiór skills, a nie źródło definicji standardu ani oficjalny katalog Anthropic. Jego instrukcje dotyczą m.in. planowania małych zmian, przeglądu implementacji, analizy złożonych tematów i budowania procedur.

Na początek przeczytaj [Feature Slice Planner](skills/feature-slice-planner/SKILL.md): zobacz, jak zapisano warunki użycia, oczekiwany wynik i kontrolę zakresu. Potem porównaj go z [Implementation Reviewer](skills/implementation-reviewer/SKILL.md), który sprawdza wykonanie wobec briefu, czyli opisu zadania. To pokazuje różnicę między instrukcją planowania a instrukcją oceny.

README opisuje katalog i sygnalizuje nieustalone prawa do pięciu wcześniejszych adaptacji. Dla czterech skills dotyczących Pythona i dostarczania zmian właściciel potwierdził pochodzenie z własnych procedur oraz udostępnienie na licencji MIT — zobacz [informacje o pochodzeniu](DRAFT-PROVENANCE.md). To potwierdzenie właściciela, nie niezależna ocena prawna; sama dostępność pliku na GitHubie nie dowodzi autorstwa ani prawa do dalszej dystrybucji.

## 5. Ograniczenia i bezpieczne korzystanie

Skill nie usuwa błędów modelu. Niejasne instrukcje, nieaktualne materiały lub brak danych mogą prowadzić do złych wyników. Testuj go na kilku prawdziwych zadaniach i sprawdzaj rezultat, zamiast oceniać jedynie płynność odpowiedzi.

**Cudzy skill traktuj jak niezweryfikowaną instrukcję i potencjalnie obcy kod.** Sam plik Markdown nie uruchamia programu, ale może nakłaniać agenta do wykonywania niebezpiecznych działań. Skrypty mogą modyfikować pliki, pobierać zależności lub wysyłać dane na zewnątrz.

Przed użyciem:

- przeczytaj `SKILL.md`, powiązane pliki i skrypty; sprawdź adresy sieciowe oraz zależności;
- nie dodawaj sekretów do współdzielonych instrukcji ani przykładów;
- udostępniaj tylko potrzebne narzędzia i dane; korzystaj z izolacji i zatwierdzania działań tam, gdzie platforma je zapewnia;
- osobno zatwierdzaj wrażliwe operacje, np. publikację, wysyłkę lub usuwanie danych;
- sprawdź licencję oraz wymagania środowiska.

Instrukcja skilla **nie powinna zastępować zgody użytkownika ani polityki uprawnień aplikacji**. Eksperymentalne pole `allowed-tools` ma różne wsparcie w klientach; nie traktuj go jako uniwersalnej bariery bezpieczeństwa.

## 6. Czytanie u źródła

1. [Introducing Agent Skills — Anthropic / Claude](https://claude.com/resources/articles/skills): przystępne ogłoszenie produktu; także datowana aktualizacja o otwartym standardzie.
2. [Equipping agents for the real world with Agent Skills — Anthropic Engineering](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills): budowa, stopniowe ładowanie, kod i zagrożenia; źródło nazwisk autorów artykułu.
3. [Agent Skills — oficjalny przegląd](https://agentskills.io/home): sens formatu, pochodzenie i ekosystem.
4. [Specyfikacja Agent Skills](https://agentskills.io/specification): wymagane pola, nazwy, zasoby i zasady organizacji — najlepszy punkt odniesienia przy pisaniu własnego skilla.
5. [Claude Platform — wpis z 16 października 2025](https://platform.claude.com/docs/en/release-notes/overview#october-16-2025): pierwotne potwierdzenie daty publicznego uruchomienia.
6. [Oficjalne wprowadzenie do MCP](https://modelcontextprotocol.io/docs/getting-started/intro): pomaga zrozumieć warstwę połączeń, odrębną od instrukcji skilla.

Najprostszy następny krok: wybierz jedną powtarzalną czynność, zapisz warunki użycia i kryterium dobrego wyniku, a potem przetestuj krótką instrukcję. Nie zaczynaj od kolekcjonowania dziesiątek skills.
